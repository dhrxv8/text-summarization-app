import streamlit as st
import sys
from text_summarization import summarize_text, summarize_uploaded_file


st.write(f"Streamlit is using this Python interpreter: {sys.executable}")

# Set up the Streamlit app
st.title("Text and Document Summarization")
st.write("Upload a file (.txt or .pdf) or enter text to summarize.")

# Text input
st.subheader("Summarize Text")
input_text = st.text_area("Enter text to summarize:")
if st.button("Summarize Text"):
    if input_text.strip():
        summary = summarize_text(input_text)
        st.success("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")

# File upload
st.subheader("Summarize Uploaded File")
uploaded_file = st.file_uploader("Upload a .txt or .pdf file:", type=["txt", "pdf"])
if st.button("Summarize File"):
    if uploaded_file:
        summary = summarize_uploaded_file(uploaded_file)
        st.success("Summary:")
        st.write(summary)
    else:
        st.warning("Please upload a file to summarize.")
