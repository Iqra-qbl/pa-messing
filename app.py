import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.home import home
from app_pages.predictor import predictor

app = MultiPage(app_name= "Cybersecurity Incident Detector") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Home", home)
app.add_page("Predictor", predictor)

app.run() # Run the  app