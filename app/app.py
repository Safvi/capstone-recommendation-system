import streamlit as st
import pandas as pd
import numpy as np
import os

# Set up Streamlit page
st.set_page_config(page_title="Book Recommender", layout="centered")

# Display current working directory (for debugging paths)
# st.write("Current working directory:", os.getcwd())

# Page Title
st.markdown("## Simple Book Recommendation System")
st.markdown("### Welcome! Select a Book and get Recommendations based on Similar Tags")

# Load books data
@st.cache_data
def load_books():
    return pd.read_csv('data/processed/05_books_with_tags.csv')

# Load cosine similarity matrix
@st.cache_data
def load_similarity():
    return np.load('data/processed/cosine_sim.npy')

books_with_tags = load_books()
cosine_sim = load_similarity()

# st.write(books_with_tags['tag_string'].head(10).tolist())

# Book selection
selected_book = st.selectbox("**Select a Book:**", books_with_tags['title'].tolist())
st.write("**Sample Book:**", selected_book)

# Show tags for selected book
selected_row = books_with_tags[books_with_tags['title'] == selected_book]
selected_tags_str = selected_row['tag_string'].values[0]
st.write("**Tags for selected book:**", selected_tags_str)

# Prepare selected book's tags
selected_tags = set(tag.strip().lower() for tag in str(selected_tags_str).split() if tag.strip())

# Find book index
try:
    selected_idx = selected_row.index[0]
except IndexError:
    st.error("Selected book not found in the dataset.")
    st.stop()

# Get similarity scores
sim_scores = list(enumerate(cosine_sim[selected_idx]))
sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

# Filter out the selected book itself
top_indices = []
for i, score in sim_scores:
    if i != selected_idx:
        top_indices.append(i)
    if len(top_indices) == 5:
        break

# Display Recommendations
st.markdown("### Top 5 Recommendations:")

for idx in top_indices:
    rec_book = books_with_tags.iloc[idx]
    title = rec_book.get('title', 'Unknown')
    author = rec_book.get('authors', 'Unknown')
    tags_str = rec_book.get('tag_string', '')
    tags = set(tag.strip().lower() for tag in str(tags_str).split() if tag.strip())

    shared_tags = selected_tags.intersection(tags)
    shared_text = ", ".join(shared_tags) if shared_tags else "No shared tags"

    st.markdown(f"🔹 **{title}** by {author}")
    st.markdown(f"➤ Shared tags: {shared_text}")
    st.markdown("---")
