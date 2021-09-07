import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from views import EDA, search, home , scatterplot

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/':
         return home.layout
    elif pathname == '/EDA':
         return EDA.layout
    elif pathname == '/search':
         return search.layout
    elif pathname == '/scatterplot':
         return scatterplot.layout
    else:
        return '404'


# Start the server
if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050", debug=False)
