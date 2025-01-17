# PDF AI Summariser

A tool that uses AI to generate summaries from PDF documents.

## Features

- AI-powered PDF summarization
- CLI interface
- Streamlit front-end for file-upload

## Prerequisites

- Python 3.12 or higher
- [Ollama](https://www.ollama.com)
- [uv](https://docs.astral.sh/uv/) (Optional)

## Installation

1. Clone the repository:
```bash
git clone 
```

2. Create a virtual environment:
```bash
python -m venv /path/to/new/virtual/environment
```
or
```bash
uv venv
```
and activate:
```bash
source .venv/bin/active
```

3. Install dependencies:
```bash
pip install -r requirements.txt 
```
or
```bash
uv pip install --requirements requirements.txt
```
4. Install an Ollama model:
```bash
ollama pull llama3.2
```
## Usage
```bash
python -m main.py <pdf_file_path> 
```
or 
```bash
uv run python main.py <pdf_file_path>
```

or use the streamlit app to select a file:
```bash
streamlit run app.py 
```