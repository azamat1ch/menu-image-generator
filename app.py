import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
import pytesseract
import io
import os
from dotenv import load_dotenv
import re

load_dotenv()

st.set_page_config(
    page_title="Menu Image Generator",
    page_icon="🍽️",
    layout="wide"
)

def setup_gemini():
    """Configure Gemini API"""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("Please set your GEMINI_API_KEY in the .env file")
        return None
    
    client = genai.Client(api_key=api_key)
    return client


def extract_text_from_image(image):
    """Extract text from uploaded image using OCR"""
    try:
        # Convert to RGB if necessary for better OCR
        if image.mode != 'RGB':
            image = image.convert('RGB')
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        st.error(f"Error extracting text from image: {str(e)}. Make sure tesseract is installed.")
        return ""

def parse_menu_items(text):
    """Parse menu text to extract individual items"""
    lines = text.split('\n')
    items = []
    
    for line in lines:
        line = line.strip()
        if line and len(line) > 3:
            # Remove prices and common formatting
            cleaned_line = re.sub(r'\$\d+\.?\d*', '', line)
            cleaned_line = re.sub(r'\d+\.?\d*', '', cleaned_line)
            cleaned_line = cleaned_line.strip(' .-')
            
            if cleaned_line:
                items.append(cleaned_line)
    
    return items

def generate_food_image_prompt(item_name):
    """Generate a detailed prompt for food image generation"""
    return f"""Create a high-quality, appetizing photograph of {item_name}. 
    The image should be professionally styled, well-lit, and show the dish in an appealing way. 
    Make it look like a restaurant-quality presentation with good composition and natural lighting.
    The food should look fresh, delicious, and inviting."""

def generate_image_with_imagen(client, prompt, image_size="512x512"):
    """Generate an image using Imagen 4"""
    try:
        # Generate image using Imagen 4
        response = client.models.generate_image(
            model='imagen-4.0-generate-preview-06-06',
            prompt=prompt,
            config=types.GenerateImageConfig(
                number_of_images=1,
                include_rai_reason=False
            )
        )
        
        # Extract image from response
        for generated_image in response.generated_images:
            if generated_image.image:
                # Convert Google Genai Image to PIL Image
                if hasattr(generated_image.image, '_pil_image'):
                    return generated_image.image._pil_image
                elif hasattr(generated_image.image, 'to_pil'):
                    return generated_image.image.to_pil()
                else:
                    # Try to get image data and convert to PIL
                    image_data = generated_image.image
                    if hasattr(image_data, 'data'):
                        return Image.open(io.BytesIO(image_data.data))
                    # If it's already a PIL Image, return it
                    return image_data
        
        return None
    except Exception as e:
        st.error(f"Error generating image: {str(e)}")
        return None

def main():
    st.title("🍽️ Menu Image Generator")
    st.markdown("Upload a menu image or enter menu items to generate food images using AI")
    
    # Initialize Gemini client
    client = setup_gemini()
    if not client:
        return
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("Settings")
        max_items = st.number_input("Max items to process", min_value=1, max_value=20, value=5)
        image_size = st.selectbox("Image size", ["256x256", "512x512", "1024x1024"], index=1)
    
    # Main interface
    tab1, tab2 = st.tabs(["📱 Upload Menu Image", "📝 Enter Menu Text"])
    
    with tab1:
        st.subheader("Upload Menu Image")
        uploaded_file = st.file_uploader("Choose a menu image", type=['png', 'jpg', 'jpeg'])
        
        if uploaded_file is not None:
            try:
                # Display uploaded image
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Menu", use_container_width=True)
            except Exception as e:
                st.error(f"Error loading image: {str(e)}")
                return
            
            # Extract text from image
            with st.spinner("Extracting text from image..."):
                extracted_text = extract_text_from_image(image)
            
            if extracted_text:
                st.subheader("Extracted Menu Text")
                st.text_area("Menu text", extracted_text, height=200)
                
                # Parse menu items
                menu_items = parse_menu_items(extracted_text)
                process_menu_items(menu_items[:max_items], client, image_size)
            else:
                st.warning("No text could be extracted from the image")
    
    with tab2:
        st.subheader("Enter Menu Items")
        menu_text = st.text_area("Paste your menu text here", height=200)
        
        if menu_text:
            menu_items = parse_menu_items(menu_text)
            process_menu_items(menu_items[:max_items], client, image_size)

def process_menu_items(menu_items, client, image_size):
    """Process menu items and generate images"""
    if not menu_items:
        st.warning("No menu items found to process")
        return
    
    st.subheader(f"Found {len(menu_items)} menu items")
    
    # Display menu items
    for i, item in enumerate(menu_items):
        st.write(f"{i+1}. {item}")
    
    if st.button("Generate Images", type="primary"):
        st.subheader("Generated Images")
        
        # Create progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Generate images for each menu item
        for i, item in enumerate(menu_items):
            status_text.text(f"Generating image for: {item}")
            progress_bar.progress((i + 1) / len(menu_items))
            
            # Generate prompt
            prompt = generate_food_image_prompt(item)
            
            # Generate image
            with st.spinner(f"Generating image for {item}..."):
                generated_image = generate_image_with_imagen(client, prompt, image_size)
            
            # Display result
            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown(f"**{item}**")
                st.markdown(f"*Size: {image_size}*")
            
            with col2:
                if generated_image:
                    try:
                        # Ensure it's a proper PIL Image
                        if not isinstance(generated_image, Image.Image):
                            st.error(f"Invalid image format for {item}")
                        else:
                            # Convert to RGB if necessary (for better Streamlit compatibility)
                            if generated_image.mode != 'RGB':
                                generated_image = generated_image.convert('RGB')
                            st.image(generated_image, caption=f"Generated image for {item}", use_container_width=True)
                    except Exception as e:
                        st.error(f"Error displaying image for {item}: {str(e)}")
                else:
                    st.error(f"Failed to generate image for {item}")
            
            st.markdown("---")
        
        status_text.text("Image generation complete!")
        st.success(f"Generated {len(menu_items)} images successfully!")

if __name__ == "__main__":
    main()