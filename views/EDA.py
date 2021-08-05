import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from views import commonmodules
import pandas as pd
df = pd.read_csv('data/tweets.csv')

from app import app

layout = html.Div([
    commonmodules.get_header(),
    commonmodules.get_menu(),   
    html.H3('Line Chart'),    
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df['created_at'], 'y': df['favorite_count'], 'type': 'line', 'name': 'Tweets Favorites'},
                {'x': df['created_at'], 'y': df['retweet_count'], 'type': 'line', 'name': 'Retweets'}
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    commonmodules.get_footer(),   
])