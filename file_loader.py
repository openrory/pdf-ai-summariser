from langchain_community.document_loaders import PyPDFLoader


def load(file_path: str) -> list:
    pages = []
    loader = PyPDFLoader(file_path)

    for page in loader.lazy_load():
        pages.append(page)
    return pages


def process_pdf(tmp_file_path):
    pages = load(tmp_file_path)
    combined_text = merge(pages)
    return pages, combined_text
    

def merge(pages) -> str:
    return "\n".join([page.page_content for page in pages])