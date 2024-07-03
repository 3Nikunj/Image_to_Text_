import streamlit as st
from PIL import Image
import pytesseract as pyt
import io

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        text = pyt.image_to_string(image)
        # Display the original image
        st.image(image, caption="Uploaded Image")
        # Display the extracted text
        st.write("Extracted Text:")
        st.write(text)
    except pyt.TesseractNotFoundError:
        st.error("Tesseract is not installed or not found. Please check the deployment configuration.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
