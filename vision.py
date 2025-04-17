from dotenv import load_dotenv
load_dotenv()
from PIL import Image  # Import Image from Pillow
import io
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(text, image):
    if not image:
        raise ValueError("No image provided.")  # This is where the error happens
    
    # Convert image to bytes
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    image_bytes = buffered.getvalue()

    # Create request content
    parts = []
    if text.strip():
        parts.append(text)
    parts.append({
        "mime_type": "image/png",
        "data": image_bytes
    })

    # Generate response
    response = model.generate_content(parts)
    return response.text

# Streamlit UI
st.set_page_config(page_title="Image Q&A Demo")
st.header("Gemini Vision Application")

input_text = st.text_input("Input Prompt:", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = None
if uploaded_file:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    except Exception as e:
        st.error(f"Error loading image: {e}")

# Debugging step: Check if image exists before processing
st.write(f"Image value: {image}")  # This line will print the current value of `image` for debugging.

if st.button("Tell me about the image"):
    if image:
        try:
            response = get_gemini_response(input_text, image)
            st.subheader("The response is:")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please upload an image first.")