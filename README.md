# PDF AI Summariser

A tool that uses AI to generate summaries from PDF documents.

## Features

- AI-powered PDF summarization
- CLI interface
- Streamlit front-end for file-upload

## Prerequisites

- Python 3.12 or higher
- [Ollama](https://www.ollama.com)
- Required dependencies:
    - python
    - langchain
    - langchain-ollama
    - pypdf
    - streamlit
    - langchain-community

## Installation

1. Clone the repository:
```bash
git clone 
```
2. Install dependencies:
```bash
pip install -r requirements.txt 
```
3. Install an Ollama model:
```bash
ollama pull llama3.2
```
## Usage
```bash
python -m main.py <pdf_file_path> 
```

or use the streamlit app to select a file:
```bash
streamlit run app.py 
```