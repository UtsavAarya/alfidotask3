import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Sample text
text = "I love this product! It's absolutely amazing."

# Analyze sentiment
sentiment = sia.polarity_scores(text)

# Print results
print("Sentiment Scores:", sentiment)

# Interpret result
compound_score = sentiment['compound']
if compound_score >= 0.05:
    print("Overall Sentiment: Positive 😊")
elif compound_score <= -0.05:
    print("Overall Sentiment: Negative 😠")
else:
    print("Overall Sentiment: Neutral 😐")
