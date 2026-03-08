# Text & Document Summarization (Streamlit + LangChain)

A lightweight Streamlit web app that summarizes either pasted text or uploaded `.txt` / `.pdf` documents using **OpenAI GPT‑3.5 (gpt-3.5-turbo)** through **LangChain**.

## What it does
- Summarizes text entered directly in the UI
- Extracts text from uploaded **PDF** files (text-based PDFs) and summarizes it
- Summarizes uploaded **TXT** files

## Tech stack
- Streamlit (UI)
- LangChain (`ChatOpenAI`, `LLMChain`)
- OpenAI API (`gpt-3.5-turbo`)
- pdfplumber (PDF text extraction)

## Demo
> Add a screenshot or GIF in `assets/` and embed it here to improve presentation.

## Project structure
- `app.py` — Streamlit UI (text input + file uploader)
- `text_summarization.py` — summarization logic + PDF/TXT handling
- `requirements.txt` — Python dependencies

## Getting started (local)

### Prerequisites
- Python 3.8+
- An OpenAI API key

### 1) Clone
```bash
git clone https://github.com/dhrxv8/text-summarization-app.git
cd text-summarization-app
```

### 2) Create and activate a virtual environment (recommended)
```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.venv\\Scripts\\activate
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Configure the OpenAI API key

This app reads the key from **Streamlit secrets** (see `text_summarization.py`).

#### Option A — Streamlit secrets (recommended)
Create a file at `.streamlit/secrets.toml`:
```toml
OPENAI_API_KEY = "your-api-key"
```

#### Option B — `.env` file (only if you update the code)
Right now `.env` loading is commented out in `text_summarization.py`. If you prefer `.env`, you can enable it by using `python-dotenv` and reading `os.getenv("OPENAI_API_KEY")`.

### 5) Run
```bash
streamlit run app.py
```

## Usage
- **Summarize Text**: paste text → click **Summarize Text**
- **Summarize File**: upload `.txt` or `.pdf` → click **Summarize File**

## Notes / limitations
- PDF extraction works best on **text-based PDFs**. Scanned/image PDFs may return little or no text.
- Long documents may take longer, cost more, or hit model token limits.
- Uploaded PDFs are temporarily written to `uploaded_file.pdf` during processing.

## Next improvements (ideas)
- Add chunking + map-reduce summarization for long documents
- Add a selector for summary length (short/medium/long)
- Add tests for the summarization functions
- Add a deployed demo link + screenshot

## License
MIT (see `LICENSE`).