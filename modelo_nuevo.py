from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
from utilities.tokenize import tokenize 
from joblib import dump, load
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from joblib import dump, load

import pandas as pd
import gzip, pickle

train_data = pd.read_csv('models/train_data.csv', encoding='utf-8')
#Transform Data Categories
di = {'P+': "P", 'N+': "N"}
train_data = train_data.replace({"polarity": di})
di2 = {'P':1, 'N': 0}
train_data = train_data.replace({"polarity": di2})
train_data = train_data.dropna()

train_data.polarity.value_counts()

import nltk
nltk.download('punkt')
nltk.download("stopwords")

#Definimos el vectorizer de nuevo y creamos un pipeline de vectorizer -> classificador
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
spanish_stopwords = stopwords.words('spanish')
#Creamos un Pipeline con los parámetros mejores
pipeline = Pipeline([
    ('vect', CountVectorizer(
            analyzer = 'word',
            tokenizer = tokenize,
            lowercase = True,
            stop_words = spanish_stopwords,
            min_df = 50,
            max_df = 1.9,
            ngram_range=(1, 1),
            max_features=1000
            )),
    ('cls', LinearSVC(C=.2, loss='squared_hinge',max_iter=1000,multi_class='ovr',
             random_state=None,
             penalty='l2',
             tol=0.0001
             )),
])

pipeline.fit(train_data.tweet, train_data.polarity)

with gzip.open('model_v3.pklz', 'wb') as ofp:
        pickle.dump(pipeline, ofp)
