import streamlit as st
import requests
import PIL.Image as Image
import os

st.set_page_config(page_title="Upload File", page_icon="📈")

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://static.vecteezy.com/system/resources/thumbnails/005/256/397/small/leaf-icon-logo-template-used-for-environment-and-plants-free-vector.jpg);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
                margin-left: 10px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "Dhanvantari";
                margin-left: 10px;
                margin-top: 500px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

add_logo()

st.title("Medicinal Plant Detection")

st.markdown("#")

on = st.toggle("Activate Camera")

if on:
    image_file = st.camera_input("Take a picture")

    if image_file is not None:
        file_details = {"FileName": image_file.name}
        img = Image.open(image_file)
        with open(image_file.name, "wb") as f:
            f.write(image_file.getbuffer())



    #if st.button('Search'):
        #st.write(classify(image_file.name))

if not on:
    image_file = st.file_uploader("Upload your file here...")

    if image_file is not None:
        file_details = {"FileName": image_file.name}
        img = Image.open(image_file)
        st.image(img)
        with open(image_file.name, "wb") as f:
            f.write(image_file.getbuffer())


def classify(img_path):

    API_URL = "https://api-inference.huggingface.co/models/Ayush7871/medicinal_plants_image_detection"
    headers = {"Authorization": "Bearer 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"}

    def query(filename):
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()

    output = query(img_path)
    if output[0]['score'] < 0.06:
        return 'Image not recognized'
    else:
        return output[0]['label']


if st.button('Search'):
    st.write(classify(image_file.name))
