# utils/embedder.py

import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.schema import Document
from langchain.embeddings import HuggingFaceEmbeddings

# Directory to save vector DB
VECTOR_STORE_DIR = "embeddings/vector_store"

def split_documents(documents, chunk_size=500, chunk_overlap=50):
    """
    Splits documents into smaller chunks for better embedding.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(documents)


def embed_documents(chunks):
    """
    Converts document chunks into embeddings using sentence-transformers.
    """
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    db = FAISS.from_documents(chunks, embeddings)
    
    # Save DB to disk
    db.save_local(VECTOR_STORE_DIR)
    print(f"[✓] Vector store saved to {VECTOR_STORE_DIR}")


def load_vector_store():
    """
    Loads the FAISS vector store from disk.
    """
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local(VECTOR_STORE_DIR, embeddings)
