
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sent(MyText):
    MySent = SentimentIntensityAnalyzer()
    MyScores = MySent.polarity_scores(MyText)

    for k, v in MyScores.items():
        print(v, k, sep = "\t")





