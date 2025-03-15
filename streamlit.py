import streamlit as st

st.title("Hello, Streamlit! 👋")
st.write("This is a simple Streamlit app.")

# Add a button
if st.button("Click Me!"):
    st.write("Button Clicked!")

# User Input
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")
