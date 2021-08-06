import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from views import commonmodules
import pandas as pd
from app import app
from utilities.search_tweets import get_tweets 

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
              State('input-2-state', 'value'))
def update_output(n_clicks, input1, input2):
    return_divs = html.Div(className='card text-white bg-primary mb-3', children=[html.Div('Tweet', className='card-header'), html.Div(className='card-body', children=[html.H4('0 Tweets', className='card-title'), html.P('There are tweets that show', className='card-text')]), ]),
    if input2 is not None:
        return_divs = []
        words = input2.split(",")
        df = get_tweets(words, input1, 'mixed', 1)
        
        for index, row in df.iterrows():
            print(row)
            return_divs.append( ( html.Div(className='card text-white bg-primary mb-3', children=[html.Div('Tweet', className='card-header'), html.Div(className='card-body', children=[html.H4(row['in_reply_to_screen_name'], className='card-title'), html.P(row['full_text'], className='card-text')]), ])))

    return return_divs
