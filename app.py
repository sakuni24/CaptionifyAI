import streamlit as st

st.title("CaptionifyAI")
st.subheader("Welcome to CaptionifyAI")

uploaded_file = st.file_uploader("Upload an image", type=["png","jpg","jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    st.write("Caption generation will be added soon")

if st.button("Generate Caption"):
    st.write("This is where your AI-generated caption will appear")