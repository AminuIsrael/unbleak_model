import pandas as pd
from statistics import mode
from CustomCode.model_predict import prediction
df = pd.read_csv("../Cleaned_data.csv")

result = []

def get_tweet_overview():
    for i in range(0,10):
        sentiment = prediction(df["tweets"][i])[0]
        result.append(sentiment)
    
    highest_occuring_sentiment = mode(result)
    
    return highest_occuring_sentiment
    