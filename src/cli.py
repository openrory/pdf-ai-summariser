import typer
from file_loader import load
from app import load_llm, generate_summary, merge
from langchain_core.messages import BaseMessage

def main(filepath: str):
    llm = load_llm()
    pages = load(filepath)
    combined_text: str = merge(pages)
    message: BaseMessage = generate_summary(llm, combined_text)
    print(message.content)
    
if __name__ == "__main__":
    typer.run(main)