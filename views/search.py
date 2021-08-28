import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from views import commonmodules
import pandas as pd
from joblib import dump, load
import pickle 
from app import app
from utilities.search_tweets import get_tweets
from models.analisis_de_sentimiento import get_result
from utilities.tokenize import tokenize 
import nltk
import gzip
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.data import load
from nltk.stem import SnowballStemmer
from string import punctuation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

class MyCustomUnpickler(pickle.Unpickler):
    print("Entrando a la funciòn")
    def find_class(self, module, name):
        print('name: ')
        print(name)
        if module == "__main__":
            print(self)
            module = "tokenize"
            print(super().find_class(module, name))
        return super().find_class(module, name)

layout = html.Div([
    commonmodules.get_header(),
    commonmodules.get_menu(),      
    html.H2('Analizer'), 
    html.P("Enter the City and a word's list separated by comma (Max: 5 words) what you want analize"),   
    dbc.Form(
        [
            dbc.FormGroup(
            [
                dbc.Label("City", className="mr-2"),
                dbc.Input(id='input-1-state', type='text', placeholder="City"),
            ],
            className="mr-3",
            ),
            dbc.FormGroup(
            [
                dbc.Label("Word List", className="mr-2"),
                dbc.Input(id="input-2-state", type='text', placeholder="Word List"),
            ],
            className="mr-3",
            ),
            dbc.FormGroup(
            [
                dbc.Label("Tweets Result Type", className="mr-2 "),
                dbc.Col(
                dbc.RadioItems(
                    id="input-3-state",
                    options=[
                        {"label": "recent", "value": "recent"},
                        {"label": "popular", "value": "popular"},
                        {"label": "mixed", "value": "mixed" },
                    ],
                ),
                width=10,
                ),
            ],
            className="mr-3",
            ),
            dbc.FormGroup(
            [
                dbc.Label("The number of times tweets are searched (each time takes 10 seconds and fetch 100 results.)", className="mr-2"),
                dcc.Dropdown(
                    id='input-4-state',
                    options=[{'label': x, 'value': x} for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
                    value=1,
                ),
            ],
        ),
        dbc.Button(id='submit-button-state', n_clicks=0, children='Submit'),
        ]
    ),
    html.Br(),
    html.Div( id='output-state'),
    commonmodules.get_footer(),

])

@app.callback(Output('output-state', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('input-1-state', 'value'),
              State('input-2-state', 'value'),
              State('input-3-state', 'value'),
              State('input-4-state', 'value'))
def update_output(n_clicks, input1, input2, input3, input4):
    return_divs = html.Div(className='card text-white bg-primary mb-3', children=[html.Div('Tweet', className='card-header'), html.Div(className='card-body', children=[html.H4('0 Tweets', className='card-title'), html.P('There are not tweets', className='card-text')]), ]),
    if input2 is not None:
        
        words = input2.split(",")
        get_tweets(words, input1, input3, input4)
        df = get_result(pd.read_csv('tweets_analizer.csv',header=0))
        print("Dataframe: ")
        print(df)
        print("-----------------------------------------------------------------------")
        #joblib.load("models/model.pkl")

        return_divs = []
        size = len(df)
        return_divs.append(html.Div(className='card text-white bg-primary mb-3', children=[html.Div('Tweet', className='card-header'), html.Div(className='card-body', children=[html.H4(str(size) + '0 Tweets', className='card-title'), html.P(' Tweets were found', className='card-text')]), ]))
        
        """ tweets_text = []
        for index, row in df.iterrows():
            try:
                tweets_text = tweets_text.append(row['full_text'])
            except: 
                pass """

        #model = load("models/model.pkl")
        """ with open('models/model.pkl', 'rb') as f:
            print("load")
            model = pickle.load(f) """
        
        """ with open('models/model.pkl', 'rb') as f:
            unpickler = MyCustomUnpickler(f)
            model = unpickler.load()

        print("Model")
        print(model) """
        #results = model.predict(array_de_textos)
        #0 = Negativo y 1= Positivo
        
        for index, row in df.iterrows():
            result_word = ''
            if row['result'] > 0:
                result_word = "Positivo"
                return_divs.append( ( html.Div(className='card text-white bg-success mb-3', children=[html.Div('Tweet', className='card-header'), html.Div(className='card-body', children=[html.H4(result_word, className='card-title'), html.P(row['full_text'], className='card-text')]), ])))
            elif row['result'] < 0:
                result_word = "Negativo"
                return_divs.append( ( html.Div(className='card text-white bg-danger mb-3', children=[html.Div('Tweet', className='card-header'), html.Div(className='card-body', children=[html.H4(result_word, className='card-title'), html.P(row['full_text'], className='card-text')]), ])))
            else:
                result_word = "Neutro"
                return_divs.append( ( html.Div(className='card text-white bg-primary mb-3', children=[html.Div('Tweet', className='card-header'), html.Div(className='card-body', children=[html.H4(result_word, className='card-title'), html.P(row['full_text'], className='card-text')]), ])))
    return return_divs
