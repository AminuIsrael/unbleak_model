#
import json
import pickle
import numpy as np
from flask import Flask, request
import warnings
warnings.filterwarnings('ignore')
from CustomCode import model_predict,total_tweet_sentiment
from tweet_scrapper import getoldtweets3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_page():
    return_data = {
        "error" : "0",
        "message" : "Successful"
    }
    return app.response_class(response=json.dumps(return_data), mimetype='application/json')

@app.route('/predict',methods=['GET'])
def get_sentiment():
    try:
        user_sentiment = request.args.get('tweet')
        if user_sentiment != None and user_sentiment != "":
            sentiment = user_sentiment
            result = model_predict.prediction(sentiment)
            status_code = 200
            return_data={
                "error": "0",
                "message": "Successfull",
                "sentiment": result[0],
                "confidence_score": result[1]
            }

        else:
            status_code = 400
            return_data = {
                "error": "1",
                "message": "Invalid Parameters"
            }
    
    except Exception as e:
        status_code = 500
        return_data = {
            'error':3,
            'message': str(e)
            }
    
    return app.response_class(response=json.dumps(return_data), mimetype='application/json'),status_code


@app.route('/sentiment',methods=["GET"])
def fetch_tweets():
    try:
        data = request.args.get('username')
        if data != None and data["username"] != "":
            #pass command to function
            getoldtweets3.main(data)
            result = total_tweet_sentiment.get_tweet_overview()
            status_code = 200
            return_data = {
                "error": "0",
                "message": "Successfull",
                "aggregate": result
                }
        else:
            status_code = 400
            return_data = {
                "error": "1",
                "message": "Invalid Parameters"
                }
    except Exception as e:
        status_code = 500
        return_data = {
            'error':3,
            'message': str(e)
            }
    
    return app.response_class(response=json.dumps(return_data), mimetype='application/json'),status_code
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=80)