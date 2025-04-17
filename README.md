# Gemini-Q-A-and-Vision-App  
Gemini-powered Q&A web app using Streamlit, supporting both text and image-based queries with Google Generative AI APIs.

## Features  
- Text Q&A using Gemini 1.5 Pro  
- Image Q&A (Vision) using Gemini 1.5 Flash  
- Simple Streamlit-based user interface  
- Supports image uploads (JPG/PNG) for visual prompts  
- Powered by Google Generative AI API

## Demo  
- `app.py` – Text Q&A interface  
- `vision.py` – Image Q&A (Vision) interface

## Getting Started  

### 1. Clone the Repository  
```bash
git clone https://github.com/yourusername/your-repo-name.git  
cd your-repo-name
```

### 2. Install Dependencies  
```bash
pip install -r requirements.txt
```
**Requirements:**  
- streamlit  
- google-generativeai  
- python-dotenv

### 3. Set Up API Key  
- Get your API key from Google AI Studio  
- Create a `.env` file in the root directory:  
```env
GOOGLE_API_KEY=your_api_key_here
```  
**Note:** Don’t commit your `.env` file to version control.

## Running the Apps  

### Text Q&A App  
```bash
streamlit run app.py
```

### Image Q&A App  
```bash
streamlit run vision.py
```

## Usage  
- For text-based questions, use the "Gemini Application" (`app.py`)  
- For image-based queries, use the "Gemini Vision Application" (`vision.py`)  
  - Upload an image  
  - Enter your prompt about the image

## File Structure  
| File             | Description                          |  
|------------------|--------------------------------------|  
| app.py           | Text Q&A Streamlit app               |  
| vision.py        | Image Q&A (Vision) Streamlit app     |  
| requirements.txt | Python dependencies                  |  
| .env             | API key (not included in repo)       |


