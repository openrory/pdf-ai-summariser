import streamlit as st
import os
import tempfile
from file_loader import load, process_pdf, merge
from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage


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


def generate_summary(llm, combined_text) -> BaseMessage:
    summary_prompt = (
        f"Please provide a concise summary of the following text: {combined_text}"
    )
    message = llm.invoke(summary_prompt)
    return message


def handle_summary_generation(combined_text):
    if st.button("Generate Summary"):
        llm = load_llm()
        with st.spinner("Generating summary..."):
            message = generate_summary(llm, combined_text)
        display_summary(message)


def display_header():
    st.title("PDF AI Summariser")
    st.write("Upload a PDF file to get an AI-generated summary")
    return st.file_uploader("Choose a PDF file", type="pdf")


def display_summary(message):
    st.subheader("Summary")
    st.write(message.content)


def display_individual_pages_expander(pages):
    with st.expander("Show Individual Pages"):
        for i, page in enumerate(pages):
            st.write(f"Page {i + 1}")
            st.write(page.page_content)


def main():
    uploaded_file = display_header()

    if uploaded_file is not None:
        tmp_file_path = create_temp_file(uploaded_file)
        try:
            with st.spinner("Processing PDF..."):
                pages, combined_text = process_pdf(tmp_file_path)
                st.info(f"Successfully processed {len(pages)} pages")
            handle_summary_generation(combined_text)
            display_individual_pages_expander(pages)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
        finally:
            os.unlink(tmp_file_path)


if __name__ == "__main__":
    main()
