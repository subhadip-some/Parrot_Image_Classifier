import streamlit as st
import numpy as np
from PIL import Image

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input


model = load_model("parrot_classifier.keras")


class_names = [
    "Amazon Green Parrot",
    "Gray Parrot",
    "Macaw",
    "White Parrot"
]


st.title("Parrot Species Classifier")

st.write("Upload a parrot image and the AI will predict its species.")


uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    image = image.resize((224, 224))

    image_array = img_to_array(image)

    image_array = np.expand_dims(image_array, axis=0)

    image_array = preprocess_input(image_array)
    predictions = model.predict(image_array)

    predicted_index = np.argmax(predictions)

    predicted_class = class_names[predicted_index]

    confidence = float(np.max(predictions) * 100)


    # results
    st.success(f"Prediction: {predicted_class}")

    st.info(f"Confidence: {confidence:.2f}%")