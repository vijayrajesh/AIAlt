# SEO Alt Text Generator

A beautiful, AI-powered tool to generate SEO-optimized alt text for images using Google Gemini API.

## Features

✨ **Multi-Image Support** - Select and process multiple images at once  
🎯 **Smart Selection** - Use Shift key to select multiple images  
🤖 **AI-Powered** - Uses Google Gemini 2.5 Flash for intelligent alt text generation  
🖼️ **Image Preview** - See thumbnails of all extracted images  
📋 **Easy Copy** - One-click copy for each generated alt text  
🎨 **Beautiful UI** - Modern glassmorphic design with smooth animations  

## Quick Start

### Prerequisites

- Python 3.6 or higher
- Google Gemini API Key ([Get it here](https://makersuite.google.com/app/apikey))

### Installation

#### Option 1: Quick Start (Windows)

1. **Double-click `start_server.bat`**
   - The batch file will automatically check for Python
   - Install required dependencies if needed
   - Start the server at `http://localhost:8000`

2. **Open your browser:**
   Navigate to `http://localhost:8000/index.html`

#### Option 2: Manual Start

1. **Install Python dependencies:**
   ```bash
   pip install requests
   ```

2. **Start the server:**
   ```bash
   python server.py
   ```

3. **Open your browser:**
   Navigate to `http://localhost:8000/index.html`

## How to Use

### Step 1: Configure API Key
1. Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Paste it in the "Settings" section
3. Click "Save" - it will be stored in your browser's localStorage

### Step 2: Fetch Images
1. Enter the article URL in the input field
2. Click "🔍 Fetch Images"
3. Wait for the tool to extract all images from the page

### Step 3: Select Images
- **Single Selection**: Click on an image
- **Multi-Selection**: Hold `Shift` and click on multiple images
- Selected images will have a purple border

### Step 4: Generate Alt Text
1. Click "🚀 Generate Alt Text (X selected)"
2. Wait for the AI to process each image
3. View the results with thumbnails and generated alt text

### Step 5: Copy & Use
- Each result has its own "📋 Copy" button
- Click to copy the alt text to your clipboard
- Paste it into your CMS or HTML

## Technical Details

### Architecture
- **Frontend**: Single HTML file with Vanilla JavaScript and Tailwind CSS
- **Backend**: Python HTTP server with CORS support and proxy endpoints
- **AI**: Google Gemini 2.5 Flash API

### Why Python Server?
The Python server solves CORS (Cross-Origin Resource Sharing) issues when fetching external images and HTML content. It provides two proxy endpoints:

- `/proxy/html?url=<URL>` - Fetches HTML content from external websites
- `/proxy/image?url=<URL>` - Fetches images from external sources

### Image Extraction
The tool extracts images from:
- `og:image` meta tag (prioritized)
- All `<img>` tags in the page
- `data-src` attributes (lazy-loaded images)

**Smart Filtering** automatically excludes:
- Small images (< 100px width or height)
- Tracking pixels (URLs containing "1x1", "pixel")
- Icons and logos

### API Usage
Each image generates one API call to Gemini with:
- **Model**: `gemini-2.5-flash-preview-09-2025`
- **Prompt**: SEO expert context with article title
- **Input**: Base64-encoded image
- **Output**: Concise alt text (max 125 characters)

## Configuration

### Change Server Port
Edit `server.py` and modify the `PORT` variable:
```python
PORT = 8000  # Change to your preferred port
```

### Customize Alt Text Prompt
Edit `index.html` and find the `callGemini` function to modify the prompt. The tool now uses article context for better results:

```javascript
// Build context-aware prompt
let promptText = `SEO Expert: Create alt text for an image in the article "${title}".`;

if (context) {
    promptText += `\n\nArticle context: ${context}`;
}

promptText += `\n\nRequirements:
- Maximum 125 characters (strict limit)
- Front-load important keywords (brands, products, locations, key subjects)
- Be specific and descriptive
- Use natural language (never start with "image of", "picture of", or "photo of")
- Optimize for SEO and accessibility
- Relate to the article context

Return ONLY the alt text, nothing else.`;
```

**What's extracted for context:**
- Meta description (og:description or meta description)
- First 3 paragraphs of main content (up to 500 characters)
- Falls back to title only if no content is found

## Troubleshooting

### Server won't start
- **Error**: `Address already in use`
  - **Solution**: Another process is using port 8000. Change the port in `server.py` or kill the process using that port.

### Images not loading
- **Error**: Failed to fetch image
  - **Solution**: Some websites block requests. Try a different article or check if the image URL is accessible.

### API errors
- **Error**: Failed to generate alt text
  - **Solution**: Check your API key, ensure you have quota remaining, and verify your internet connection.

### No images found
- **Error**: No images found in the article
  - **Solution**: The article might not have images, or they're loaded dynamically with JavaScript. Try a different URL.

## File Structure

```
AKAAlt/
├── index.html          # Main application (HTML + CSS + JS)
├── server.py           # Python HTTP server with CORS
├── start_server.bat    # Windows batch file for easy startup
└── README.md           # This file
```

## Browser Compatibility

- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Opera

## Security Notes

- API keys are stored in browser's localStorage (client-side only)
- The Python server runs locally and is not exposed to the internet
- Never share your Gemini API key publicly

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits

Built with ❤️ using:
- [Google Gemini AI](https://ai.google.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Python](https://www.python.org/)

---

**Need help?** Check the console for error messages or review the troubleshooting section above.
