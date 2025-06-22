# app/ui_streamlit.py

import streamlit as st
import sys
import os

# ✅ Add the root directory to the path so it can find 'chains/'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from chains.rag_qa_chain import build_qa_chain

# Initialize chatbot logic
run_query = build_qa_chain()

# Streamlit UI setup
st.set_page_config(page_title="Personal Assistant Chatbot", page_icon="🤖")
st.title("🧠 Your Personal Q&A Assistant")
st.markdown("Ask me about fitness, academics, general knowledge, or daily tips!")

# Session chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User Input
user_input = st.text_input("📝 Ask me something:", key="input")

if user_input:
    with st.spinner("Thinking... 🤔"):
        answer = run_query(user_input)

    # Save to session history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", answer))

# Display chat history
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**🧍 You:** {message}")
    else:
        st.markdown(f"**🤖 Assistant:** {message}")
