# utils/llm_setup.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_llm():
    return genai.GenerativeModel("gemini-pro")
