# utils/loader.py

import wikipedia
from langchain.schema import Document
import os

# Optional: Uncomment below if you want to add PDF support later
# from langchain.document_loaders import PyPDFLoader


def load_wikipedia_articles(topics: list) -> list:
    """
    Load multiple Wikipedia articles and convert to LangChain Documents.
    """
    documents = []
    for topic in topics:
        try:
            summary = wikipedia.summary(topic, sentences=10)  # Get a summary
            doc = Document(page_content=summary, metadata={"source": "wikipedia", "topic": topic})
            documents.append(doc)
        except Exception as e:
            print(f"[!] Error loading {topic}: {e}")
    return documents


def load_text_file(file_path: str) -> list:
    """
    Load a local text file and convert to LangChain Document.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    return [Document(page_content=content, metadata={"source": file_path})]


# Optional: Enable this later if using PDFs
# def load_pdf(file_path: str) -> list:
#     """
#     Load a PDF file using LangChain's PyPDFLoader.
#     """
#     loader = PyPDFLoader(file_path)
#     return loader.load()
