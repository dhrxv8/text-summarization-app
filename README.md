# Text & Document Summarization (Streamlit + LangChain + OpenAI)

A simple Streamlit web app that summarizes **plain text** or **uploaded `.txt` / `.pdf` files** using **`gpt-3.5-turbo`** via LangChain.

## Features

- Summarize text pasted into the app
- Upload and summarize `.txt` files
- Upload and summarize `.pdf` files (extracts text with `pdfplumber`)
- Minimal UI built with Streamlit

## Tech Stack

- **UI:** Streamlit
- **LLM Orchestration:** LangChain (`ChatOpenAI`, `PromptTemplate`, `LLMChain`)
- **Model:** OpenAI `gpt-3.5-turbo`
- **PDF Text Extraction:** `pdfplumber`

## How it works (high-level)

1. Streamlit collects either:
   - text from a text area, or
   - an uploaded file (`.txt` / `.pdf`)
2. For PDFs, text is extracted from each page via `pdfplumber`.
3. The app sends the text to a LangChain summarization prompt:
   - `Summarize the following text: ...`
4. The OpenAI model returns a summary that’s displayed in the UI.

## Project Structure

- `app.py` — Streamlit UI
- `text_summarization.py` — summarization logic + PDF extraction helpers
- `requirements.txt` — pinned dependencies

## Setup (Local)

### Prerequisites

- Python **3.8+**
- An OpenAI API key

### 1) Clone

```bash
git clone https://github.com/dhrxv8/text-summarization-app.git
cd text-summarization-app
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Configure your OpenAI API key (required)

This project currently reads the key from **Streamlit secrets**:

- Create a file at: `.streamlit/secrets.toml`
- Add:

```toml
OPENAI_API_KEY = "your-api-key-here"
```

### 4) Run the app

```bash
streamlit run app.py
```

Then open the local URL Streamlit prints in your terminal.

## Usage

### Summarize Text
1. Paste text into the text box
2. Click **Summarize Text**
3. The summary appears below

### Summarize File
1. Upload a `.txt` or `.pdf` file
2. Click **Summarize File**
3. The summary appears below

## Notes / Limitations

- **Large PDFs** may exceed model context limits and/or become slow/costly (no chunking implemented yet).
- **Scanned PDFs** without an embedded text layer may return little/no text (OCR not implemented).
- When summarizing PDFs, the current implementation writes the upload to `uploaded_file.pdf` locally.

## License

MIT — see `LICENSE`.
