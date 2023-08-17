import streamlit as st
import streamlit.components.v1 as components
from textblob import TextBlob
from PIL import Image
import text2emotion as te
import plotly.graph_objects as go
import requests
import json
import modals
import pandas as pd

# Streamlit App
def renderPage():
st.title("Twitter Sentiment Analysis")

# Upload a CSV file containing the Twitter data
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the uploaded CSV file into a DataFrame
    data = pd.read_csv(uploaded_file)

    # Analyze sentiments
    data['Sentiment'] = data['Text'].apply(lambda x: TextBlob(x).sentiment.polarity)

    # Categorize sentiments
    data['Sentiment_Category'] = data['Sentiment'].apply(lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Neutral')

    # Display sentiment analysis results
    st.write("Sentiment Analysis Results:")
    st.write(data['Sentiment_Category'].value_counts())

    # Display the uploaded dataset with sentiment analysis
    st.write("Uploaded Dataset with Sentiment Analysis:")
    st.write(data)


