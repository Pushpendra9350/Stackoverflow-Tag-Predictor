import pandas as pd
import numpy as np
import re
from tqdm import tqdm
import warnings
import nltk
nltk.download('punkt')
warnings.filterwarnings("ignore")
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import joblib
from joblib import load
from flask_ngrok import run_with_ngrok
from flask import Flask, request, render_template
app = Flask(__name__)

# Stopwords list 
stop_words = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"}

# This will work as a text spliter 
def text_splitter(text):
    return text.split()

# To load model, Vectorizer and tag list 
model = joblib.load("stackoverflow_model_100k.pkl")
vectorizer = joblib.load("stackoverflow_tfidf_vectorizer_100k.pkl")
tags = pd.read_csv("tag_list.csv")
tag_list = tags["Tags"].to_list()

# Data Preprocessing for new question
def text_preprocessing(title,question):
    # Stemmer is converting like: eating --> eat or running --> run
    stemmer = SnowballStemmer("english")

    # To replace <code>...</code> with space " "
    question=re.sub('<code>(.*?)</code>', '', question, flags=re.MULTILINE|re.DOTALL)

    # To remove all HTML tags from questions
    html_cleaner = re.compile('<.*?>')
    question = re.sub(html_cleaner, ' ', str(question.encode("utf-8")))
    
    title=title.encode('utf-8')
        
    # Concatinate title and question
    question=str(title)+" "+str(question)   

    # To remove all characters instead of alphabets
    question=re.sub(r'[^A-Za-z]+',' ',question)

    # First, we convert all text to lowercase and Word tokenize will convert 
    # "This is data preprocessing" --> ["This","is","data","preprocessing"]
    words=word_tokenize(str(question.lower()))

    # Removing all single letter and stopwords from question except letter 'c' because c is a prog. language
    # After removing all single words join then with space
    question= ' '.join(str(stemmer.stem(j)) for j in words if j not in stop_words and (len(j)!=1 or j=='c'))
    return question

# To predict results 
def predict1(title,question):

    # Step 1: Text preprocessing
    fine_text = text_preprocessing(title,question)

    # Step 2: Make transform of your text to features 
    vector = vectorizer.transform([fine_text])

    # Step 3: Predict outputs 
    prediction = model.predict(vector)

    # Get the array of the prediction
    prediction_results = prediction.toarray()[0]
    final_tags = []

    # Find relevent tags according to the results 
    for i in range(5500):
        if prediction_results[i]==1:
            final_tags.append(tag_list[i])
    return final_tags

# Home page 
@app.route('/')
def homepage():
    return render_template('index.html')

# To get input from frontend and send the results to frontend 
@app.route('/', methods= ["POST"])
def background_process():
    if request.method == 'POST':
        title = request.form.get('title')
        question = request.form.get('question')
        result = predict1(title,question)
        if len(result) == 0:
            result = ["Not Find Any Results"]
        if title:
            result1 = tuple(result)
            return render_template('index.html',result1 = result)
        else:
            return render_template('index.html',error='Please provide atleast title to get results')

# To start the application
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port="5000")