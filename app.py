# Load your libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pyjokes
import os

# Create the app
external_stylesheets = external_stylesheets=[dbc.themes.COSMO]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Start the server
if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050", debug=True)