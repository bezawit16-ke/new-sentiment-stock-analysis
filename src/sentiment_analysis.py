# Sentiment Analysis Functions
def analyze_sentiment(text):
    from textblob import TextBlob
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def clean_text(text):
    return str(text).lower().strip()
