import random
import streamlit as st

# Function to generate band name
def generate_bandname(words):
    word1 = random.choice(words)
    word2 = random.choice(words)
    while word1 == word2:
        word2 = random.choice(words)
    return f"{word1} {word2}"

# Streamlit user interface
st.title("Band Name Generator🎸🎺🎹")
st.write("-------------------------------")

# Getting user input
user_words = st.text_area("Enter some fancy words for your band's name (Minimum 3 words & comma-separated):", "Electric,Harmonic,Mystic,Waves,Dragons,Eclipse")

# Splitting the input into a list
words = [word.strip() for word in user_words.split(',')]

if st.button("Generate Band Names"):
    st.write("Here are some band names for you:")
    for _ in range(5):
        st.write(generate_bandname(words))
