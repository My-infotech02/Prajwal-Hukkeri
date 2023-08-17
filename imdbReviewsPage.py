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




getEmoji = {
    "happy" : "😊",
    "neutral" : "😐",
    "sad" : "😔",
    "disgust" : "🤢",
    "surprise" : "😲",
    "fear" : "😨",
    "angry" : "😡",
    "positive": "🙂",
    "neutral": "😐",
    "negative": "☹️",
}


# Streamlit App
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

def plotPie(labels, values):
    fig = go.Figure(
        go.Pie(
        labels = labels,
        values = [value*100 for value in values],
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    st.plotly_chart(fig, use_container_width=True)

lastSearched = ""
cacheData = {}
        




    
                    
                

def applyModal(movie, packageName):
    if(packageName == "Flair"):
        predictionList = [modals.flair(review) for review in movie["reviews"]]
        valueCounts = dict(pd.Series(predictionList).value_counts())
        print(valueCounts)
        return valueCounts
    elif(packageName == "TextBlob"):
        predictionList = [modals.textBlob(review) for review in movie["reviews"]]
        valueCounts = dict(pd.Series(predictionList).value_counts())
        print(valueCounts)
        return valueCounts
    elif(packageName == "Vader"):
        predictionList = [modals.vader(review) for review in movie["reviews"]]
        valueCounts = dict(pd.Series(predictionList).value_counts())
        print(valueCounts)
        return valueCounts
    elif(packageName == "Text2emotion"):
        predictionList = [modals.text2emotion(review) for review in movie["reviews"]]
        valueCounts = dict(pd.Series(predictionList).value_counts())
        print(valueCounts)
        return valueCounts
    else:
        return ""
    

def renderPage():
    st.title("Sentiment Analysis 😊😐😕😡")
    components.html("""<hr style="height:3px;border:none;color:#333;background-color:#333; margin-bottom: 10px" /> """)
    # st.markdown("### User Input Text Analysis")
    st.subheader("IMDb movie review analysis")
    st.text("Analyze movie reviews from IMDb API for sentiments.")
    st.text("")
    movieName = st.text_input('Movie Name', placeholder='Input name HERE')
    packageName = st.selectbox(
     'Select Package',
     ('Flair', 'Vader', 'TextBlob', 'Text2emotion'))
    if st.button('Search'):
        if movieName:
            process(movieName, packageName)
        else:
            st.warning("Please enter a movie name")
