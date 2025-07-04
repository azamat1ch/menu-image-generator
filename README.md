# Menu Image Generator 🍽️

A Streamlit web application that generates high-quality images for menu items using Google's Imagen 4 AI model. Perfect for restaurants and food businesses who want to visualize their menu items with professional-looking food photography.

## Features

- **Menu Image Upload**: Upload photos of menus and extract text using OCR
- **Manual Menu Entry**: Type or paste menu items directly
- **Smart Menu Parsing**: Automatically extracts and cleans menu items, removing prices and formatting
- **AI Image Generation**: Uses Google Imagen 4 to generate realistic food images
- **Robust Error Handling**: Graceful handling of API failures and image processing errors
- **Batch Processing**: Generate multiple images with progress tracking
- **Configurable Settings**: Adjust image size and processing limits
- **Clean Interface**: Modern Streamlit UI with tabs and customizable settings

## Tech Stack

- **Python 3.9+** (with Streamlit compatibility constraints)
- **Streamlit** - Web UI framework
- **Google Genai** - Google's AI API for Imagen 4 image generation
- **Tesseract OCR** - Text extraction from menu images
- **Pillow** - Image processing and conversion
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

3. **Install Tesseract OCR**:
   - **Ubuntu/Debian**: `sudo apt-get install tesseract-ocr`
   - **macOS**: `brew install tesseract`
   - **Windows**: Download from [GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki)

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your Google AI API key:
   ```
   GEMINI_API_KEY=your_google_ai_api_key_here
   ```

5. **Get a Google AI API key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Add it to your `.env` file

## Usage

1. **Run the application**:
   ```bash
   poetry run streamlit run app.py
   ```

2. **Open your browser** and go to `http://localhost:8501`

3. **Configure settings** (optional):
   - Set maximum number of items to process
   - Choose image size (256x256, 512x512, or 1024x1024)

4. **Choose your input method**:
   - **Upload Menu Image**: Take a photo of a menu or upload an image file
   - **Enter Menu Text**: Type or paste menu items directly

5. **Generate Images**: Click "Generate Images" to create AI-generated food images

## How It Works

1. **Text Extraction**: If you upload an image, the app uses Tesseract OCR to extract text
2. **Menu Parsing**: The extracted text is cleaned and parsed to identify individual menu items
3. **Prompt Generation**: Each menu item is converted into a detailed prompt for food photography
4. **AI Generation**: Prompts are sent to Google's Imagen 4 model for high-quality image generation
5. **Image Processing**: Generated images are converted to PIL format and displayed with proper error handling
6. **Display**: Generated images are displayed alongside the original menu items with progress tracking

## Project Structure

```
menu-image-generator/
├── app.py                 # Main Streamlit application
├── pyproject.toml         # Poetry dependencies and configuration
├── README.md             # Project documentation
├── .env.example          # Environment variables template
└── .env                  # Your API keys (not tracked in git)
```

## Key Functions

- `setup_gemini()` - Initialize Google Genai client
- `extract_text_from_image()` - OCR text extraction with error handling
- `parse_menu_items()` - Clean and parse menu text
- `generate_food_image_prompt()` - Create detailed prompts for AI generation
- `generate_image_with_imagen()` - Generate images using Imagen 4
- `process_menu_items()` - Batch process menu items with progress tracking

## Requirements

- Python 3.9+ (excluding 3.9.7 for Streamlit compatibility)
- Tesseract OCR installed on your system
- Google AI API key with Imagen 4 access
- Internet connection for API calls

## Error Handling

The application includes robust error handling for:
- Invalid or corrupted image files
- OCR processing failures
- API rate limits and failures
- Image format conversion issues
- Missing dependencies

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and ensure code quality
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Recent Updates

- ✅ **Google Genai Integration**: Switched to google-genai package for improved API compatibility
- ✅ **Imagen 4 Support**: Full image generation capability using Google's latest model
- ✅ **Enhanced Error Handling**: Comprehensive error handling for all operations
- ✅ **Image Processing**: Robust PIL Image conversion and RGB handling
- ✅ **Dependency Updates**: Updated Python version constraints for Streamlit compatibility

## Future Enhancements

- [ ] Multiple image styles (photography, illustration, etc.)
- [ ] Export functionality for generated images
- [ ] Multi-language support for menu text
- [ ] Advanced menu parsing with categories
- [ ] Batch export in various formats
- [ ] Integration with restaurant POS systems