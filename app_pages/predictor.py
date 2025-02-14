import streamlit as st
import pandas as pd
import time
from joblib import load as load_model

def predictor():
    # Load the pipeline, as we'll begin predicting on page load with the default values
    pipeline = load_model("models/logistic_regression_pipeline.pkl")

    st.write("Enter your data to predict the threat in real time.")

    # Initialize session state for prediction and probability
    if "prediction" not in st.session_state:
        st.session_state.prediction = 0
    if "probability" not in st.session_state:
        st.session_state.probability = 0

    # Function to run prediction when input changes
    def input_changed():
        print("Input changed")

        # Fetch latest input values from session state
        data = pd.DataFrame({
            "network_packet_size": [st.session_state.network_packet_size],
            "protocol_type": [st.session_state.protocol_type],
            "login_attempts": [st.session_state.login_attempts],
            "session_duration": [st.session_state.session_duration],
            "encryption_used": [st.session_state.encryption_used],
            "ip_reputation_score": [st.session_state.ip_reputation_score],
            "failed_logins": [st.session_state.failed_logins],
            "browser_type": [st.session_state.browser_type],
            "unusual_time_access": [bool(st.session_state.unusual_time_access == "Yes")]
        })
        
        print(data)

        # Predict the threat
        prediction = pipeline.predict(data)
        probability = pipeline.predict_proba(data)[0][1]

        print(f"Prediction: {prediction[0]}")

        # Update session state
        st.session_state.prediction = prediction[0]
        st.session_state.probability = probability

    # Organize the widgets in 2 columns
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("Enter the network packet size:", 
                        value=1500, min_value=0, key="network_packet_size", on_change=input_changed)
        st.number_input("Enter the number of login attempts:", 
                        value=1, min_value=0, key="login_attempts", on_change=input_changed)
        st.number_input("Enter the session duration in milliseconds:", 
                        value=1500, min_value=0, key="session_duration", on_change=input_changed)
        st.number_input("Enter the IP reputation score (from 0 to 1):", 
                        value=0.5, min_value=0.0, max_value=1.0, key="ip_reputation_score", on_change=input_changed)
        st.number_input("Enter the number of failed logins:", 
                        value=0, min_value=0, key="failed_logins", on_change=input_changed)

    with col2:
        st.selectbox("Select the protocol type:", ["TCP", "UDP", "ICMP"], 
                     key="protocol_type", on_change=input_changed)
        st.selectbox("Select if encryption is used:", ["AES", "DES", "unknown"], 
                     key="encryption_used", on_change=input_changed)
        st.selectbox("Select the browser type:", ["Chrome", "Firefox", "Safari", "Edge", "Opera", "unknown"], 
                     key="browser_type", on_change=input_changed)
        st.selectbox("Select if unusual time access:", ["Yes", "No"], 
                     key="unusual_time_access", on_change=input_changed)

    # Display prediction results
    st.title(f"Prediction: {"Safe" if not st.session_state.prediction else "Attack!"}")
    st.write(f"Probability of attack: {st.session_state.probability * 100.0:.2f}%")

    # Update the progress bar dynamically
    st.progress(st.session_state.probability)
