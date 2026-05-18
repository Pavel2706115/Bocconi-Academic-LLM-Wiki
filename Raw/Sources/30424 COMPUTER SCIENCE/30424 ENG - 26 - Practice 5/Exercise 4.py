

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

MySent = SentimentIntensityAnalyzer()

sentences = ["I like Python",
             "I like Python!",
             "I love Python",
             "I like Python???",
             "I like Python :(",
             "I like Python and hate coding",
             "I like Python but hate coding",
             "I hate coding but like Python"]


