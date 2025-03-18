import requests
from transformers import pipeline
from gtts import gTTS
from bs4 import BeautifulSoup
import newspaper

# Fetch news articles related to the company
def fetch_news(company_name):
    articles = []
    search_url = f"https://news.google.com/search?q={company_name}&hl=en"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract article links
    links = soup.find_all('a', {'class': 'DY5T1d'})
    for link in links[:10]:
        article_url = "https://news.google.com" + link['href'][1:]
        article = get_article_details(article_url)
        if article:
            articles.append(article)
    return articles

def get_article_details(url):
    article = {}
    try:
        news_article = newspaper.Article(url)
        news_article.download()
        news_article.parse()

        article['title'] = news_article.title
        article['summary'] = news_article.summary
        article['source'] = news_article.source_url
        article['content'] = news_article.text

        return article
    except Exception as e:
        print(f"Failed to fetch article {url}: {str(e)}")
        return None

# Perform sentiment analysis on articles
def analyze_sentiment(articles):
    sentiment_analyzer = pipeline("sentiment-analysis")
    sentiments = []
    for article in articles:
        sentiment = sentiment_analyzer(article['content'])[0]
        sentiments.append({
            'title': article['title'],
            'sentiment': sentiment['label'],
            'confidence': sentiment['score']
        })
    return sentiments

# Generate TTS audio in Hindi
def generate_tts(text):
    tts = gTTS(text, lang='hi')
    audio_file = "tts_audio.mp3"
    tts.save(audio_file)
    return audio_file
