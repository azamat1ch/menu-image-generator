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

def main():
    st.title("🍽️ Menu Image Generator")
    st.markdown("Upload a menu image or enter menu items to generate food images using AI")
    
    # Initialize Gemini
    model = setup_gemini()
    if not model:
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
                process_menu_items(menu_items[:max_items], model)
            else:
                st.warning("No text could be extracted from the image")
    
    with tab2:
        st.subheader("Enter Menu Items")
        menu_text = st.text_area("Paste your menu text here", height=200)
        
        if menu_text:
            menu_items = parse_menu_items(menu_text)
            process_menu_items(menu_items[:max_items], model)

def process_menu_items(menu_items, model):
    """Process menu items and generate images"""
    if not menu_items:
        st.warning("No menu items found to process")
        return
    
    st.subheader(f"Found {len(menu_items)} menu items")
    
    # Display menu items
    for i, item in enumerate(menu_items):
        st.write(f"{i+1}. {item}")
    
    if st.button("Generate Images", type="primary"):
        # Note: Gemini Pro doesn't support image generation yet
        # This is a placeholder for when image generation becomes available
        st.info("🚧 Image generation feature coming soon!")
        st.markdown("Currently, Gemini Pro doesn't support image generation. This feature will be available when Google releases Gemini Pro Vision with image generation capabilities.")
        
        # For now, show what would be generated
        st.subheader("Preview: Items to Generate")
        cols = st.columns(2)
        
        for i, item in enumerate(menu_items):
            with cols[i % 2]:
                st.markdown(f"**{item}**")
                st.markdown(f"*Prompt: {generate_food_image_prompt(item)}*")
                st.markdown("---")

if __name__ == "__main__":
    main()