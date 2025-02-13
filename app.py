# a simple streamlit app which just shows a welcome message

import streamlit as st


def main():
    st.title("Cybersecurity Threat Detection")
    st.write("This is a simple app which uses Streamlit to create a web app for cybersecurity threat detection.")
    
    st.write("Here's the correlation heatmap of the dataset:")
    
    # Display an image from the filesystem
    st.image("images/heatmap.png", width=700)


if __name__ == "__main__":
    main()
