import streamlit as st
from PIL import Image
import pytesseract
import io

# Create a file uploader widget
uploaded_file = st.file_uploader(
    "Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image using PIL
    image = Image.open(uploaded_file)

    # Convert the image to text
    text = pytesseract.image_to_string(image)

    # Display the original image
    st.image(image, caption="Uploaded Image")

    # Display the extracted text
    st.write("Extracted Text:")
    st.write(text)
