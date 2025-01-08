import streamlit as st
from caption_generator import generate_caption
from PIL import Image

st.title("CaptionifyAI")
st.subheader("Welcome to CaptionifyAI")

uploaded_file = st.file_uploader("Upload an image", type=["png","jpg","jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

if st.button("Generate Caption"):
    if uploaded_file:
        temp_image_path = "temp_image.jpg"
        with open(temp_image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        caption = generate_caption(temp_image_path)
        st.write("Generated Caption:")
        st.write(caption)
    else:
        st.write("Please upload an image first!")