<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>RAG Personal Assistant Chatbot</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: #f7f9fc;
      color: #222;
      padding: 40px;
      line-height: 1.7;
      max-width: 900px;
      margin: auto;
    }
    h1, h2, h3 {
      color: #2b6cb0;
    }
    pre {
      background: #eee;
      padding: 12px;
      border-radius: 8px;
      overflow-x: auto;
    }
    code {
      background-color: #f0f0f0;
      padding: 3px 6px;
      border-radius: 4px;
      font-family: Consolas, monospace;
    }
    ul {
      margin-left: 1.5em;
    }
    .highlight {
      background: #d9f2ff;
      padding: 8px 12px;
      border-left: 4px solid #2b6cb0;
      margin: 10px 0;
    }
  </style>
</head>
<body>

  <h1>🤖 RAG-Based Personal Assistant Chatbot</h1>

  <p>
    A smart, responsive Q&A chatbot built with <strong>LangChain + FAISS + HuggingFace + Streamlit</strong>.
    It can answer general knowledge, news, fitness tips, and academic questions — all from your local knowledge base.
  </p>

  <h2>🚀 Features</h2>
  <ul>
    <li>Conversational Q&A interface</li>
    <li>Context-aware answers from your data</li>
    <li>Semantic search with FAISS</li>
    <li>Clean UI with Streamlit</li>
  </ul>

  <h2>📁 Project Structure</h2>
  <pre><code>
RAG_ChatBot_PA/
├── app/
│   └── ui_streamlit.py
├── chains/
│   └── rag_qa_chain.py
├── utils/
│   ├── loader.py
│   ├── embedder.py
│   └── creator.py
├── data/
│   └── your_knowledge.txt
├── vector_db/
├── .env
└── README.md
  </code></pre>

  <h2>⚙️ Setup Instructions</h2>

  <h3>1. Clone the Repository</h3>
  <pre><code>git clone https://github.com/your-username/RAG_ChatBot_PA.git
cd RAG_ChatBot_PA</code></pre>

  <h3>2. Create & Activate Environment</h3>
  <pre><code>python -m venv venv
venv\Scripts\activate</code></pre>

  <h3>3. Install Requirements</h3>
  <pre><code>pip install -r requirements.txt</code></pre>

  <h3>4. Add <code>.env</code> File</h3>
  <pre><code>API_KEY=your_api_key_here
MODEL_TYPE=huggingface</code></pre>

  <h2>🧠 Build the Vector Store</h2>
  <p>Put your data in <code>data/your_knowledge.txt</code> and run:</p>
  <pre><code>python utils/creator.py</code></pre>

  <h2>💬 Launch the Chatbot</h2>
  <pre><code>streamlit run app/ui_streamlit.py</code></pre>

  <h2>📚 Sample Knowledge Base Format</h2>
  <pre><code>
Q: What is the capital of France?
A: Paris.

Q: How many calories in 1 banana?
A: About 105 calories.

Q: What is Machine Learning?
A: A subset of AI that learns from data.
  </code></pre>

  <h2>📦 requirements.txt</h2>
  <pre><code>
langchain
langchain-community
sentence-transformers
faiss-cpu
streamlit
python-dotenv
  </code></pre>

  <h2>✅ TODO</h2>
  <ul>
    <li>Add website/PDF ingestion</li>
    <li>Deploy on HuggingFace</li>
    <li>Use Gemini or OpenRouter APIs</li>
    <li>Add voice or memory feature</li>
  </ul>

  <h2>👨‍💻 Author</h2>
  <p>
    Built with 💙 by <strong>Your Name</strong>  
    <br>Follow on GitHub and share if useful!
  </p>

  <h2>🛡️ License</h2>
  <p>
    MIT License. Free for personal and commercial use.
  </p>

</body>
</html>
