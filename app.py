import streamlit as st
import sidebar
import textPage
# import audioPage
import pandas as pd
from textblob import TextBlob

import imagePage
# import videoPage
#import twitterAnalysisPage

# st.title("Hello")
page = sidebar.show()

if page=="Text":
    textPage.renderPage()
# elif page=="Audio":
#     audioPage.renderPage()
elif page="Twitter":
        st.title("Twitter Sentiment Analysis")
        components.html("""<hr style="height:3px;border:none;color:#333;background-color:#333; margin-bottom: 10px" /> """)

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
    
elif page=="Image":
    imagePage.renderPage()
# elif page=="Video":
#     videoPage.main()
#elif page=="Twitter Data":
 #    twitterAnalysisPage.renderPage()
