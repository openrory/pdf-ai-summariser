from langchain_community.document_loaders import PyPDFLoader

def load(file_path: str) -> list:
    pages = []
    loader = PyPDFLoader(file_path)
    
    for page in loader.lazy_load():
        pages.append(page)
    return pages
