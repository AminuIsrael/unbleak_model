import pickle
from .data_preprocessing import clean_tweets,tokenizer
from sklearn.feature_extraction.text import HashingVectorizer
import numpy as np

model_path = './ML_model/model.pkl'

#
def prediction(text):
    text = clean_tweets(text)
    vect = HashingVectorizer(decode_error='ignore', n_features=2**21, 
                                     preprocessor=None,tokenizer=tokenizer)
    clf = pickle.load(open(model_path, 'rb'))
    X = vect.transform([text])
    label = {0:'negative', 1:'positive'}
    prediction = clf.predict(X)[0]
    confidence_score = round(np.max(clf.predict_proba(X))*100,2)
    
    return label[prediction],confidence_score