from utilities.tokenize import tokenize 
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import pandas as pd
import nltk
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline


def get_modelo():
        train_data = pd.read_csv('data/train_data.csv', encoding='utf-8')
        #Transform Data Categories
        di = {'P+': "P", 'N+': "N"}
        train_data = train_data.replace({"polarity": di})
        di2 = {'P':1, 'N': 0}
        train_data = train_data.replace({"polarity": di2})
        train_data = train_data.dropna()

        train_data.polarity.value_counts()

        #Definimos el vectorizer de nuevo y creamos un pipeline de vectorizer -> classificador
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

        return pipeline.fit(train_data.tweet, train_data.polarity)          
