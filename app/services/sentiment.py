import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Téléchargement des ressources NLTK nécessaires (à faire lors de la première exécution)
def download_nltk_resources():
    try:
        nltk.data.find('sentiment/vader_lexicon.zip')
    except LookupError:
        nltk.download('vader_lexicon')

# Analyse du sentiment d'un texte avec VADER
def analyze_sentiment(text):
    # S'assurer que les ressources sont téléchargées
    download_nltk_resources()
    
    # Initialiser l'analyseur de sentiments
    sia = SentimentIntensityAnalyzer()
    
    # Obtenir les scores de polarité pour le texte
    sentiment_scores = sia.polarity_scores(text)
    
    return sentiment_scores