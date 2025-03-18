import streamlit as st
from api import fetch_news, analyze_sentiment, generate_tts
from utils import get_comparative_analysis

def main():
    st.title("Company News Sentiment Analysis and TTS")
    
    #company name
    company_name = st.text_input("Enter Company Name", "BlackRock")
    
    if company_name:
        # atricles related to company
        st.write(f"Fetching news articles for {company_name}...")
        news_articles = fetch_news(company_name)
        
        if not news_articles:
            st.write("No news articles found.")
            return
        
        # extracted news articles
        st.write(f"### Extracted News Articles for {company_name}:")
        for article in news_articles:
            st.write(f"**{article['title']}**")
            st.write(f"Summary: {article['summary']}")
            st.write(f"Source: {article['source']}")
            st.write("-" * 50)

        # to do sentiment analysis
        sentiments = analyze_sentiment(news_articles)
        
        # comparative analysis
        comparative_result = get_comparative_analysis(sentiments)
        
        # Display sentiment comparison
        st.write("### Sentiment Analysis Report")
        st.write(f"Sentiment Distribution: {comparative_result}")
        
        # Convert the summary to Hindi TTS
        tts_audio = generate_tts("Sentiment summary: " + str(comparative_result))
        st.audio(tts_audio)


