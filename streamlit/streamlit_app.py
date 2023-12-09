import os
import streamlit as st
import requests

# Streamlit webpage title
st.title('Sentiment Analysis Interface')

# Text input for the user
user_input = st.text_area("Enter text to analyze sentiment")

APP_URL = os.environ.get("APP_URL", "0.0.0.0:8000")

# Function to send text to FastAPI and get back the task ID
def analyze_sentiment(text):
    response = requests.post(f"http://{APP_URL}/analyze-sentiment/", json={"text": text})
    return response.json()

# Function to get task status and result
def get_task_result(task_id):
    response = requests.get(f"http://{APP_URL}/task/{task_id}")
    return response.json()

# Button to send text to FastAPI
if st.button('Analyze'):
    if user_input:
        task_info = analyze_sentiment(user_input)
        task_id = task_info['task_id']
        st.write(f"Task ID: {task_id}")

        # Polling the task status
        st.write("Analyzing sentiment...")
        result = get_task_result(task_id)
        while result['status'] != 'completed':
            result = get_task_result(task_id)
        st.write("Analysis complete!")
        st.write(f"Result: {result['result']}")
    else:
        st.write("Please enter some text to analyze.")
