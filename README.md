# Menu Image Generator 🍽️

A Streamlit web application that generates images for menu items using Google's Gemini AI. Perfect for restaurants and food businesses who want to visualize their menu items when descriptions aren't enough.

## Features

- **Menu Image Upload**: Upload photos of menus and extract text using OCR
- **Manual Menu Entry**: Type or paste menu items directly
- **Smart Menu Parsing**: Automatically extracts and cleans menu items, removing prices and formatting
- **AI Image Generation**: Uses Google Gemini API to generate food images (coming soon)
- **Clean Interface**: Modern Streamlit UI with tabs and customizable settings

## Tech Stack

- **Python 3.9+**
- **Streamlit** - Web UI framework
- **Google Generative AI** - Gemini API for AI capabilities
- **Tesseract OCR** - Text extraction from images
- **Pillow** - Image processing
- **Poetry** - Dependency management

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd menu-image-generator
   ```

2. **Install dependencies using Poetry**:
   ```bash
   poetry install
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Get a Gemini API key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Add it to your `.env` file

## Usage

1. **Run the application**:
   ```bash
   poetry run streamlit run app.py
   ```

2. **Open your browser** and go to `http://localhost:8501`

3. **Choose your input method**:
   - **Upload Menu Image**: Take a photo of a menu or upload an image file
   - **Enter Menu Text**: Type or paste menu items directly

4. **Generate Images**: Click "Generate Images" to create AI-generated food images

## How It Works

1. **Text Extraction**: If you upload an image, the app uses Tesseract OCR to extract text
2. **Menu Parsing**: The extracted text is cleaned and parsed to identify individual menu items
3. **AI Generation**: Each menu item is sent to Gemini AI with a detailed prompt for food image generation
4. **Display**: Generated images are displayed alongside the original menu items

## Current Status

⚠️ **Note**: Image generation is currently a placeholder feature. Google Gemini Pro doesn't yet support image generation. This feature will be activated once Google releases Gemini with image generation capabilities.

## Requirements

- Python 3.9 or higher
- Tesseract OCR installed on your system
- Google Gemini API key
- Internet connection for API calls

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Future Enhancements

- [ ] Image generation once available in Gemini
- [ ] Multiple image styles (photography, illustration, etc.)
- [ ] Batch processing for large menus
- [ ] Export functionality for generated images
- [ ] Multi-language support
- [ ] Advanced menu parsing with categories