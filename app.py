import streamlit as st
import google.generativeai as genai
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
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-pro')

def setup_imagen():
    """Configure Imagen 4 for image generation"""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("Please set your GEMINI_API_KEY in the .env file")
        return None
    
    genai.configure(api_key=api_key)
    # Use the correct model name for Imagen 4
    return genai.GenerativeModel('gemini-2.0-flash-exp')

def extract_text_from_image(image):
    """Extract text from uploaded image using OCR"""
    try:
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        st.error(f"Error extracting text from image: {str(e)}")
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

def generate_image_with_imagen(model, prompt, image_size="512x512"):
    """Generate an image using Imagen 4"""
    try:
        # Generate image using Imagen 4
        # According to Google AI documentation, use the generate_images method
        response = genai.generate_images(
            model='imagen-4',
            prompt=prompt,
            number_of_images=1,
            safety_filter_level="default",
            person_generation="dont_allow",
            aspect_ratio="1:1",
            quality="standard"
        )
        
        # Extract image from response
        if response.images and len(response.images) > 0:
            # Get the first generated image
            image_data = response.images[0]
            
            # Convert to PIL Image if it's bytes
            if isinstance(image_data, bytes):
                return Image.open(io.BytesIO(image_data))
            elif hasattr(image_data, 'image'):
                return image_data.image
            else:
                return image_data
        
        return None
    except Exception as e:
        st.error(f"Error generating image: {str(e)}")
        return None

def main():
    st.title("🍽️ Menu Image Generator")
    st.markdown("Upload a menu image or enter menu items to generate food images using AI")
    
    # Initialize Gemini for text processing
    text_model = setup_gemini()
    if not text_model:
        return
    
    # Initialize Imagen for image generation
    image_model = setup_imagen()
    if not image_model:
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
            # Display uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Menu", use_column_width=True)
            
            # Extract text from image
            with st.spinner("Extracting text from image..."):
                extracted_text = extract_text_from_image(image)
            
            if extracted_text:
                st.subheader("Extracted Menu Text")
                st.text_area("Menu text", extracted_text, height=200)
                
                # Parse menu items
                menu_items = parse_menu_items(extracted_text)
                process_menu_items(menu_items[:max_items], image_model, image_size)
            else:
                st.warning("No text could be extracted from the image")
    
    with tab2:
        st.subheader("Enter Menu Items")
        menu_text = st.text_area("Paste your menu text here", height=200)
        
        if menu_text:
            menu_items = parse_menu_items(menu_text)
            process_menu_items(menu_items[:max_items], image_model, image_size)

def process_menu_items(menu_items, image_model, image_size):
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
                generated_image = generate_image_with_imagen(image_model, prompt, image_size)
            
            # Display result
            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown(f"**{item}**")
                st.markdown(f"*Size: {image_size}*")
            
            with col2:
                if generated_image:
                    st.image(generated_image, caption=f"Generated image for {item}", use_column_width=True)
                else:
                    st.error(f"Failed to generate image for {item}")
            
            st.markdown("---")
        
        status_text.text("Image generation complete!")
        st.success(f"Generated {len(menu_items)} images successfully!")

if __name__ == "__main__":
    main()