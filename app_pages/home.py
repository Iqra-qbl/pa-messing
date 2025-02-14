import streamlit as st


def home():
    st.write("This is a simple app which uses Streamlit to create a web app for cybersecurity threat detection.")
    
    st.write("Here's the correlation heatmap of the dataset:")
    
    # Display an image from the filesystem
    st.image("images/heatmap.png", width=700)