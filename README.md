
This project implements a web-based text summarization tool using GPT-3.5 and LangChain, integrated into a Streamlit app. Users can either input text directly or upload a `.txt` or `.pdf` file for summarization. The app uses the OpenAI API to summarize the provided text or documents.

## Features
- **Summarize Text:** Input text to generate a summary.
- **Summarize File:** Upload a `.txt` or `.pdf` file, and the app will extract the text and summarize it.

## Installation

To set up and run the project locally, follow these steps:

### Prerequisites
- Python 3.8+
- OpenAI API key (get your API key from https://beta.openai.com/)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/text-summarization-app
   cd text-summarization-app

   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - You can set the API key in the `secrets` of your Streamlit app by adding your OpenAI API key as `OPENAI_API_KEY`.
   
   Or, if you are running the project locally, you can use a `.env` file with the following content:
   ```bash
   OPENAI_API_KEY=your-api-key-here
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

### Supported File Types
- `.txt`
- `.pdf`

### App Overview
- **Text Input:** Enter text directly in the input box, then click "Summarize Text" to get a summary.
- **File Upload:** Upload a `.txt` or `.pdf` file and click "Summarize File" to get a summary of its content.

## Usage

1. **Summarize Text:**
   - Enter the text you want to summarize in the input field.
   - Click the **Summarize Text** button, and the summary will appear below.

2. **Summarize File:**
   - Upload a `.txt` or `.pdf` file.
   - Click the **Summarize File** button, and the summary will be generated.

## Example

1. **Text Input:**
   - Input: "The quick brown fox jumps over the lazy dog."
   - Output: "A fast fox leaps over a lazy dog."

2. **File Upload:**
   - Upload a `.pdf` document with content, and the app will extract and summarize the text from the document.

## Dependencies

The project uses the following Python packages:
- `streamlit==1.26.0`: For creating the web app interface.
- `langchain==0.0.304`: For summarization and integration with GPT-3.5.
- `openai==0.27.8`: For accessing OpenAI's GPT-3.5 API.
- `pdfplumber==0.10.2`: For extracting text from PDF files.
- `python-dotenv==1.0.0`: For loading environment variables.
- `tenacity==8.2.2`: For handling retry logic in case of API rate limits.
- `tiktoken==0.4.0`: Required for token handling with LangChain.

## License

This project is licensed under the MIT License.
