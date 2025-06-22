# chains/rag_qa_chain.py

from utils.embedder import load_vector_store
from utils.llm_setup import get_llm

def build_qa_chain():
    """
    Loads vector DB and Gemini model to create a QA chain.
    """
    vectorstore = load_vector_store()
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    model = get_llm()  # Gemini model

    def run_query(query: str):
        # Retrieve top 3 relevant chunks
        docs = retriever.get_relevant_documents(query)
        context = "\n".join([doc.page_content for doc in docs])

        # Prompt Gemini with context + query
        prompt = f"""
You are a helpful assistant. Use the following information to answer the question.

Context:
{context}

Question: {query}
Answer:"""

        response = model.generate_content(prompt)
        return response.text.strip()

    return run_query
