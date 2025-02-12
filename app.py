# a simple streamlit app which just shows a welcome message

import streamlit as st


def main():
    st.title("Welcome to Streamlit")
    st.write("This is a simple Streamlit app which just shows a welcome message.")
    
if __name__ == "__main__":
    
    main()