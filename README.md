# Text & Document Summarization App

A Streamlit app that summarizes pasted text or uploaded `.txt` / `.pdf` files using LangChain and OpenAI.

## Overview

This is an educational AI application project focused on wiring together a simple user interface, document text extraction, prompt templating, and an OpenAI-backed summarization chain.

The app is intentionally small: it demonstrates the end-to-end workflow from upload/input to summary output, while keeping the implementation easy to inspect.

## Features

- Summarize text pasted into the app
- Upload and summarize `.txt` files
- Upload and summarize text-based `.pdf` files
- Extract PDF text with `pdfplumber`
- Store the OpenAI API key in Streamlit secrets

## Tech Stack

| Layer | Tools |
|---|---|
| UI | Streamlit |
| LLM orchestration | LangChain (`ChatOpenAI`, `PromptTemplate`, `LLMChain`) |
| Model | `gpt-3.5-turbo` as configured in the current code |
| PDF extraction | pdfplumber |
| Runtime | Python |

## How It Works

1. Streamlit collects text from a text area or file uploader.
2. `.txt` files are decoded directly.
3. `.pdf` files are written temporarily and parsed with `pdfplumber`.
4. The extracted text is passed into a LangChain prompt.
5. OpenAI returns a summary that is displayed in the Streamlit UI.

## Project Structure

```text
text-summarization-app/
├── app.py                  # Streamlit UI
├── text_summarization.py   # Summarization and PDF extraction logic
├── requirements.txt        # Pinned dependencies
└── README.md
```

## Setup

### Prerequisites

- Python 3.8+
- An OpenAI API key

### 1. Clone

```bash
git clone https://github.com/dhrxv8/text-summarization-app.git
cd text-summarization-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

Create `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "your-api-key-here"
```

### 4. Run

```bash
streamlit run app.py
```

## Limitations

- Large PDFs may exceed model context limits because chunking is not implemented.
- Scanned PDFs without embedded text are not supported because OCR is not implemented.
- The current implementation writes uploaded PDFs to a temporary local file named `uploaded_file.pdf`.
- The project uses older LangChain/OpenAI dependency versions and should be upgraded before production use.

## Status

Educational demo. Useful for showing a simple AI app workflow, but not intended as a production document-processing system without chunking, OCR, stronger file handling, and dependency upgrades.

## License

MIT — see `LICENSE`.
