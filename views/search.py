import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from views import commonmodules
import pandas as pd 
from app import app
from utilities.search_tweets import get_tweets
from models.model_e import get_result
from models.model_v import get_modelo
import time


layout = html.Div([
    commonmodules.get_header(),
    commonmodules.get_menu(),
    dbc.Container([ 
        html.Br(),
        html.Br(),     
        html.H1('Analizer', className='text-center font-weight-bold'),
        html.Br(),
        html.Br(),
        html.H3("Follow the instructions: "), 
        html.Div(children=[
                html.Iframe( "allowfullscreen"
                    ,className="embed-responsive-item" 
                    ,src="assets/img/video.mp4" 
                )]
            ,className="embed-responsive embed-responsive-21by9"
        ),
        html.Br(),
        html.Br(),
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
            dbc.Button(id='submit-button-state', n_clicks=0, children='Submit')
            ]
        ),
        html.Br(),
        html.Br(),
        dbc.Row(dbc.Col(
            dbc.Spinner(children=[html.Div( id='output-state'),], 
            size="lg", color="primary", type="border", fullscreen=True,),
            width={'size': 12, 'offset': 0}),
        ),
        #html.Div( id='output-state'),
        html.Br(),
        ]),
    commonmodules.get_footer()
])

@app.callback(Output('output-state', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('input-1-state', 'value'),
              State('input-2-state', 'value'),
              State('input-3-state', 'value'),
              State('input-4-state', 'value'))
def update_output(n_clicks, input1, input2, input3, input4):
    return_divs = []
    time = 0
    return_divs.append(html.Br())
    return_divs.append(html.Div(className='card text-white bg-primary mb-3', children=[html.Div('Tweet', className='card-header'), html.Div(className='card-body', children=[html.H4('0 Tweets', className='card-title'), html.P('There are not tweets', className='card-text')]), ]))
    if input2 is not None:
        time = 25
        words = input2.split(",")
        get_tweets(words, input1, input3, input4)
        df_result = pd.read_csv('data/tweets_analizer.csv',header=0)
        
        try:
            modelo_v
        except:
            modelo_v = get_modelo()
        
        df = get_result(pd.read_csv('data/tweets_analizer.csv',header=0))
        df.to_csv('data/results_tweets_analizer.csv', index=False)
        time = 50
        df['polarity_v'] = modelo_v.predict(df_result['full_text'])
        time = 100

        return_divs = []
        size = len(df)
        return_divs.append(html.Div(className='card text-white bg-primary mb-3', 
        children=[html.Div('Tweet', className='card-header'), 
        html.Div(className='card-body', 
            children=
                [html.H4(str(size) + 'Tweets', className='card-title'), 
                 html.P(' Tweets were found', className='card-text'),
                 dcc.Link("Show Graphs",href="/scatterplot", className="btn btn-primary stretched-link")
                ]), 
        ]))
        
        for index, row in df.iterrows():
            result_word = ''
            return_divs.append(html.Hr())
            if row['result'] > 0:
                result_word = "Positivo"
                return_divs.append( ( html.Div(className='card text-white bg-success mb-3', children=[html.Div('Tweet analized by Model E', className='card-header'), html.Div(className='card-body', children=[html.H4(result_word, className='card-title'), html.P(row['full_text'], className='card-text')]), ])))
                if row['polarity_v']> 0:
                    return_divs.append( ( html.Div(className='card text-white bg-success mb-3', children=[html.Div('Tweet analized by Modelo V', className='card-header'), html.Div(className='card-body', children=[html.H4(result_word, className='card-title'), html.P(row['full_text'], className='card-text')]), ])))                    
                else:
                    result_word = "Negativo"
                    return_divs.append( ( html.Div(className='card text-white bg-danger mb-3', children=[html.Div('Tweet analized by Modelo V', className='card-header'), html.Div(className='card-body', children=[html.H4(result_word, className='card-title'), html.P(row['full_text'], className='card-text')]), ])))
            
            elif row['result'] < 0:
                result_word = "Negativo"
                return_divs.append( ( html.Div(className='card text-white bg-danger mb-3', children=[html.Div('Tweet analized by Model E', className='card-header'), html.Div(className='card-body', children=[html.H4(result_word, className='card-title'), html.P(row['full_text'], className='card-text')]), ])))
                if row['polarity_v']< 0:
                    return_divs.append( ( html.Div(className='card text-white bg-danger bg-success mb-3', children=[html.Div('Tweet analized by Modelo V', className='card-header'), html.Div(className='card-body', children=[html.H4(result_word, className='card-title'), html.P(row['full_text'], className='card-text')]), ])))                    
                else:
                    result_word = "Positivo"
                    return_divs.append( ( html.Div(className='card text-white bg-success mb-3', children=[html.Div('Tweet analized by Modelo V', className='card-header'), html.Div(className='card-body', children=[html.H4(result_word, className='card-title'), html.P(row['full_text'], className='card-text')]), ])))
            else:
                result_word = "Neutro"
                return_divs.append( ( html.Div(className='card text-white bg-primary mb-3', children=[html.Div('Tweet analized by Model E', className='card-header'), html.Div(className='card-body', children=[html.H4(result_word, className='card-title'), html.P(row['full_text'], className='card-text')]), ])))
                if row['polarity_v']< 0:
                    result_word = "Negativo"
                    return_divs.append( ( html.Div(className='card text-white bg-danger mb-3', children=[html.Div('Tweet analized by Modelo V', className='card-header'), html.Div(className='card-body', children=[html.H4(result_word, className='card-title'), html.P(row['full_text'], className='card-text')]), ])))                    
                else:
                    result_word = "Positivo"
                    return_divs.append( ( html.Div(className='card text-white bg-success mb-3', children=[html.Div('Tweet analized by Modelo V', className='card-header'), html.Div(className='card-body', children=[html.H4(result_word, className='card-title'), html.P(row['full_text'], className='card-text')]), ])))
            return_divs.append(html.Hr())        
    return return_divs
