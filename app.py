import streamlit as st
import os
import tempfile
from file_loader import load
from langchain_ollama import ChatOllama


def create_temp_file(uploaded_file) -> str:
    """Create a temporary file from the uploaded file."""
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        return tmp_file.name


def load_llm():
    """Load the LLM model."""
    return ChatOllama(
        model="llama3.2",
        temperature=0.8,
        num_predict=256,
    )


def generate_summary(llm, combined_text):
    with st.spinner("Generating summary..."):
        summary_prompt = (
            f"Please provide a concise summary of the following text: {combined_text}"
        )
        message = llm.invoke(summary_prompt)
        return message


def display_summary(message):
    st.subheader("Summary")
    st.write(message.content)


def show_individual_pages_expander(pages):
    with st.expander("Show Individual Pages"):
        for i, page in enumerate(pages):
            st.write(f"Page {i + 1}")
            st.write(page.page_content)


def merge(pages) -> str:
    return "\n".join([page.page_content for page in pages])


def setup_page():
    st.title("PDF AI Summariser")
    st.write("Upload a PDF file to get an AI-generated summary")
    return st.file_uploader("Choose a PDF file", type="pdf")


def process_pdf(tmp_file_path):
    with st.spinner("Processing PDF..."):
        pages = load(tmp_file_path)
        combined_text = merge(pages)
        st.info(f"Successfully processed {len(pages)} pages")
        return pages, combined_text


def handle_summary_generation(combined_text):
    if st.button("Generate Summary"):
        llm = load_llm()
        message = generate_summary(llm, combined_text)
        display_summary(message)


def main():
    uploaded_file = setup_page()

    if uploaded_file is not None:
        tmp_file_path = create_temp_file(uploaded_file)
        try:
            pages, combined_text = process_pdf(tmp_file_path)
            handle_summary_generation(combined_text)
            show_individual_pages_expander(pages)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
        finally:
            os.unlink(tmp_file_path)


if __name__ == "__main__":
    main()
