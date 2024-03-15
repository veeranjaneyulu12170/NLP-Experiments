
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
def analyze_sentiment(review):
    # NLTK's SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    nltk_sentiment = sia.polarity_scores(review)

    # TextBlob's sentiment analysis
    tb_sentiment = TextBlob(review).sentiment

    # Determine overall sentiment based on compound score from NLTK
    sentiment = ""
    if nltk_sentiment['compound'] >= 0.05:
        sentiment = "Positive 😀"
    elif nltk_sentiment['compound'] <= -0.05:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    return nltk_sentiment, tb_sentiment, sentiment
# Example movie review
review = "I absolutely loved this movie! The acting was superb and the plot kept me on the edge of my seat the whole time. Definitely recommend it to everyone. 👍"

# Analyze sentiment
nltk_sentiment, tb_sentiment, overall_sentiment = analyze_sentiment(review)

# Output results
print("NLTK Sentiment Analysis:", nltk_sentiment)
print("TextBlob Sentiment Analysis:", tb_sentiment)
print("Overall Sentiment:", overall_sentiment)
NLTK Sentiment Analysis: {'neg': 0.0, 'neu': 0.625, 'pos': 0.375, 'compound': 0.9298}
TextBlob Sentiment Analysis: Sentiment(polarity=0.41500000000000004, subjectivity=0.54)
Overall Sentiment: Positive 😀
 
