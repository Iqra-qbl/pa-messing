# a simple streamlit app which just shows a welcome message

import streamlit as st
import pandas as pd
import time
from joblib import load as load_model


def predictor():

    # Load the pipeline, as we'll begin predicting on page load with 
    # the default values
    pipeline = load_model("models/logistic_regression_pipeline.pkl")

    st.write("Enter your data to predict the threat in real time.")

    if "prediction" not in st.session_state:
        st.session_state.prediction = 0
    if "probability" not in st.session_state:
        st.session_state.probability = 0
    

    # Run the prediction when the button is clicked
    def input_changed():
        print("Input changed")
        # Run the prediction
        # Create a DataFrame from the user inputs
        data = pd.DataFrame({
            "network_packet_size": [network_packet_size],
            "protocol_type": [protocol_type],
            "login_attempts": [login_attempts],
            "session_duration": [session_duration],
            "encryption_used": [encryption_used],
            "ip_reputation_score": [ip_reputation_score],
            "failed_logins": [failed_logins],
            "browser_type": [browser_type],
            "unusual_time_access": [bool(unusual_time_access == "Yes")]
        })
        # Predict the threat
        prediction = pipeline.predict(data)
        print(f"Prediction: {prediction[0]}")
        # Display the prediction in the UI
        st.session_state.prediction = prediction[0]
        st.session_state.probability = pipeline.predict_proba(data)[0][1]


    # Create widgets for user input for these features:['network_packet_size', 'protocol_type', 'login_attempts',
    #   'session_duration', 'encryption_used', 'ip_reputation_score',
    #   'failed_logins', 'browser_type', 'unusual_time_access',
    # Organize the widgets in 2 columns
    col1, col2 = st.columns(2)
    with col1:
        network_packet_size = st.number_input(
            "Enter the network packet size:",
            value=1500, min_value=0, on_change=input_changed
        )
        login_attempts = st.number_input(
            "Enter the number of login attempts:",
            value=1, min_value=0, on_change=input_changed
        )
        session_duration = st.number_input(
            "Enter the session duration in milliseconds:",
            value=1500, min_value=0, on_change=input_changed
        )
        ip_reputation_score = st.number_input(
            "Enter the IP reputation score (from 0 to 1):",
            value=0.5, min_value=0.0, max_value=1.0, on_change=input_changed
        )
        failed_logins = st.number_input(
            "Enter the number of failed logins:",
            value=0, min_value=0, on_change=input_changed
        )

    with col2:
        protocol_type = st.selectbox(
            "Select the protocol type:", ["TCP", "UDP", "ICMP"],
            on_change=input_changed
        )
        encryption_used = st.selectbox(
            "Select if encryption is used:", ["AES", "DES", "unknown"],
            on_change=input_changed
        )
        browser_type = st.selectbox(
            "Select the browser type:", ["Chrome", "Firefox", "Safari", "Edge", "Opera", "unknown"],
            on_change=input_changed
        )
        unusual_time_access = st.selectbox(
            "Select if unusual time access:", ["Yes", "No"],
            on_change=input_changed
        )

    # Create placeholders for prediction and probability display
    st.title(f"Prediction: {"Safe" if not st.session_state.prediction else "Attack!"}")
    st.write(f"Probability: {st.session_state.probability * 100.0:.2f}%")


    probability_display = st.progress(st.session_state.probability)







