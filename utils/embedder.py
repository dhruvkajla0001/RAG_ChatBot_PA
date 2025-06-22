from utils.loader import load_wikipedia_articles, load_text_file

# Load Wikipedia topics
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

wiki_docs = load_wikipedia_articles(topics)

# Load a local .txt file
# text_docs = load_text_file("data/raw/fitness_tips.txt")

# Final all docs list
# all_docs = wiki_docs + text_docs
