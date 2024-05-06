import streamlit as st
import requests
import PIL.Image as Image
import numpy as np
from PIL import Image
from numpy import asarray
import tensorflow as tf
from tensorflow import keras
import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory

path = r"archive/Train/Train"
train = image_dataset_from_directory(path, batch_size=32,
                                    image_size=(256,256),shuffle=True)
class_labels = train.class_names
model = keras.models.load_model('model.h5', custom_objects=None, compile=True, safe_mode=True)

def Prediction(model, img):
    img_array = tf.keras.preprocessing.image.img_to_array((img))
    img_array = tf.expand_dims(img_array, 0)  # create a batch

    predictions = model.predict(img_array)

    predicted_class = class_labels[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)

    return predicted_class, confidence


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

    imgs = Image.open(img_path)
    predicted_class , confidence = Prediction(model,asarray(imgs))

    if confidence < 0.06:
        return 'Image not recognized'
    else:
        return predicted_class


if st.button('Search'):
    st.write(classify(image_file.name))
