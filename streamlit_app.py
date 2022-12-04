import streamlit as st
from PIL import Image
import requests

st.title("Codepan Coding Challenge")

upload_img = st.file_uploader(label='Upload your Image', type=['jpg', 'jpeg'], accept_multiple_files=False)

if upload_img:

    img = Image.open(upload_img)
    st.image(img, caption="Your Image", use_column_width=True)
    files = {"file": upload_img.getvalue()}
    res = requests.post(f"http://localhost:8000/score", files=files)
    st.write(res.json())
