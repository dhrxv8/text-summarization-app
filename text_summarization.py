import os
import pdfplumber
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
#from dotenv import load_dotenv
import streamlit as st
import openai

# Set your OpenAI API Key directly in the code
# Load environment variables from the .env file
#load_dotenv()

# Access the OpenAI API key from the environment
#os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
openai.api_key = st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

# Define a prompt for summarization
summarization_prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text:\n\n{text}"
)

# Create a summarization chain
summarization_chain = LLMChain(llm=llm, prompt=summarization_prompt)


def summarize_text(input_text):
    """
    Summarizes the given text using GPT-3.5.

    Args:
        input_text (str): The text to summarize.

    Returns:
        str: The summarized text or an error message.
    """
    try:
        if not input_text.strip():
            return "Input text is empty. Please provide valid text for summarization."
        # Run the summarization chain
        summary = summarization_chain.run({"text": input_text})
        return summary
    except Exception as e:
        return f"An error occurred while summarizing the text: {e}"


def summarize_pdf(file_path):
    """
    Extracts text from a PDF file and summarizes its content.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        str: The summarized content or an error message.
    """
    try:
        # Extract text from the PDF
        with pdfplumber.open(file_path) as pdf:
            text = "".join(page.extract_text() or "" for page in pdf.pages)

        if not text.strip():
            return "The PDF contains no readable text."

        # Summarize the extracted text
        return summarize_text(text)
    except FileNotFoundError:
        return "The PDF file was not found. Please check the file path."
    except Exception as e:
        return f"An error occurred while summarizing the PDF: {e}"


# Streamlit integration
def summarize_uploaded_file(uploaded_file):
    """
    Handles file uploads and summarizes the content if it is a text or PDF file.

    Args:
        uploaded_file: Uploaded file object.

    Returns:
        str: The summarized content or an error message.
    """
    try:
        # Check the file type
        if uploaded_file.name.endswith(".txt"):
            # Handle plain text files
            input_text = uploaded_file.read().decode("utf-8")
            return summarize_text(input_text)
        elif uploaded_file.name.endswith(".pdf"):
            # Handle PDF files
            with open("uploaded_file.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())
            return summarize_pdf("uploaded_file.pdf")
        else:
            return "Unsupported file type. Please upload a .txt or .pdf file."
    except Exception as e:
        return f"An error occurred while processing the uploaded file: {e}"
