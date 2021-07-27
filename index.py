import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from views import linechart, barchart, home , scatterplot

app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return home.layout
    elif pathname == '/linechart':
         return linechart.layout
    elif pathname == '/barchart':
         return barchart.layout
    elif pathname == '/scatterplot':
         return scatterplot.layout
    else:
        return '404'


# Start the server
if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050", debug=True)
