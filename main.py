from utils.loader import load_wikipedia_articles
from utils.embedder import split_documents, embed_documents

topics = [
    "Protein foods",
    "Exercise for beginners",
    "Recursion in programming",
    "Newton's Laws of Motion",
    "India",
    "Artificial Intelligence",
    "Mental health tips",
    "Sleep and productivity"
]

docs = load_wikipedia_articles(topics)

chunks = split_documents(docs)
embed_documents(chunks)  # Saves FAISS store
