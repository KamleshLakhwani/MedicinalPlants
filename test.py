import numpy as np
from PIL import Image
from numpy import asarray
import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense,Dropout,Conv2D, Flatten,MaxPooling2D
from keras.models import Sequential
from tensorflow.keras.preprocessing import image_dataset_from_directory
from huggingface_hub import from_pretrained_keras
from tensorflow.keras.preprocessing import image_dataset_from_directory

path = r"archive/Train/Train"
train = image_dataset_from_directory(path, batch_size=32,
                                    image_size=(256,256),shuffle=True)

#pathx=r"C:\Projects\Junk\model.keras"

class_labels = train.class_names

#model = keras.models.load_model("model.h5")
model = keras.models.load_model('model.h5', custom_objects=None, compile=True, safe_mode=True)
#print(model.summary())

#imgs = Image.open('basil.jpg')

def calling(img_path):
    imgs = Image.open('basil.jpg')
    predicted_class, confidence = Prediction(model, asarray(imgs))
    return predicted_class


#print('hello')
def Prediction(model, img):
    img_array = tf.keras.preprocessing.image.img_to_array((img))
    img_array = tf.expand_dims(img_array, 0)  # create a batch

    predictions = model.predict(img_array)

    predicted_class = class_labels[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)

    return predicted_class, confidence
    #return predicted_class
    #return predictions

#predicted_class , confidence = Prediction(model,asarray(imgs))
#pred = Prediction(model,asarray(imgs))
#print(predicted_class)



#print('hello2')
