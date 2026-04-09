import cv2
import numpy as np
import streamlit as st
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
from PIL import Image
import pandas as pd


def load_model():
    model = MobileNetV2(weights="imagenet")
    return model


def preprocess_image(image):
    img = np.array(image)
    img = cv2.resize(img, (224, 224))
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)
    return img


def classify_image(model, image, top_n=3):
    try:
        processed_image = preprocess_image(image)
        predictions = model.predict(processed_image)
        decoded_predictions = decode_predictions(predictions, top=top_n)[0]
        return decoded_predictions
    except Exception as e:
        st.error(f"Error classifying image: {str(e)}")
        return None


def translate_label(label):
    translations = {
        "dog": "cachorro",
        "cat": "gato",
        "car": "carro",
        "person": "pessoa"
    }
    return translations.get(label, label)


def main():
    st.set_page_config(page_title="AI Image Classifier", page_icon="🖼️", layout="centered")

    st.title("🖼️ AI Image Classifier")
    st.write("Upload an image and let AI tell you what is in it!")

    @st.cache_resource
    def load_cached_model():
        return load_model()

    model = load_cached_model()

    # Sidebar
    st.sidebar.header("Settings")
    top_n = st.sidebar.slider("Number of predictions", 1, 10, 3)
    translate = st.sidebar.checkbox("Translate labels to Portuguese")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Info da imagem
        st.info(f"Image size: {image.size} | Mode: {image.mode}")

        if st.button("Classify Image"):
            with st.spinner("Analyzing Image..."):
                predictions = classify_image(model, image, top_n)

                if predictions:
                    st.subheader("Predictions")

                    results = []
                    for _, label, score in predictions:
                        label_display = translate_label(label) if translate else label
                        st.write(f"**{label_display}**: {score:.2%}")
                        results.append({"Label": label_display, "Confidence": score})

                    # Tabela
                    df = pd.DataFrame(results)
                    st.dataframe(df)

                    # Gráfico
                    st.subheader("Confidence Chart")
                    st.bar_chart(df.set_index("Label"))

                    # Download
                    csv = df.to_csv(index=False).encode("utf-8")
                    st.download_button(
                        "Download Results",
                        csv,
                        "predictions.csv",
                        "text/csv"
                    )


if __name__ == "__main__":
    main()