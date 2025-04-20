import streamlit as st

# Imran Khan's books list (simple format)
books = [
    "Pakistan: A Personal History (2011)",
    "Indus Journey (1990)", 
    "Warrior Race (1993)"
]

# App title
st.title("📚 Imran Khan's Books")

# Show all books
st.write("### All Books")
for book in books:
    st.write(f"- {book}")

# Select a book
selected = st.selectbox("Pick a book to learn more:", books)

# Show selected book details
if selected:
    st.write(f"You selected: **{selected}**")
    
    # Simple description based on selection
    if "Pakistan" in selected:
        st.write("This book talks about Pakistan's history")
    elif "Indus" in selected:
        st.write("This book describes the Indus Valley")
    else:
        st.write("This book is about tribal cultures")

# Simple reading list
if 'my_books' not in st.session_state:
    st.session_state.my_books = []

if st.button("Add to My List"):
    if selected not in st.session_state.my_books:
        st.session_state.my_books.append(selected)
        st.success("Added!")
    else:
        st.warning("Already in your list")

# Show my list
if st.session_state.my_books:
    st.write("### My Reading List")
    for book in st.session_state.my_books:
        st.write(f"- {book}")
else:
    st.info("Your list is empty")
