import streamlit as st
from PIL import Image
import pytesseract as pyt
import io

uploaded_file = st.file_uploader(
    "Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    pyt.pytesseract.tesseract_cmd = "tesseract.exe"
    text = pyt.image_to_string(image)

    # Display the original image
    st.image(image, caption="Uploaded Image")

    # Display the extracted text
    st.write("Extracted Text:")
    st.write(text)
