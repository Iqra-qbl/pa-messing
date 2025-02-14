import streamlit as st
import pandas as pd


def home():

    sample_data = pd.read_csv("data/first_five_rows.csv")
    sample_data.drop(columns=["Unnamed: 0"], inplace=True)

    st.header("An app to aid cybersecurity incident detection")
    st.write(
        "The data set was sourced from Kaggle and contains information about "
        "network traffic and cybersecurity threats. The goal is to predict whether "
        "a network session is a threat or not."
    )

    # Create a table with the features of the dataset
    st.subheader("Sample of original dataset")
    st.dataframe(sample_data)

    # Feature importance section
    st.subheader("Feature importance")
    st.write(
        "The following features are the most important for predicting cybersecurity threats."
        "They are listed in descending order of importance, by absolute value."
    )
    st.image("images/feature_importance.png", width=700)


    st.write("Here's the correlation heatmap of the dataset:")
    
    # Display an image from the filesystem
    st.image("images/heatmap.png", width=700)