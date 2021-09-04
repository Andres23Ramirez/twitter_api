import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash_html_components.Header import Header

from views import commonmodules

from app import app

""" header = html.H1('DS4A - Twittycs.ml', className='text-center')
    return header """

def get_header():
    header =    html.Div(children=[  
                    html.Div(children=[   
                            html.Div(
                                    "DS4A / Colombia - Cohort 5",
                                    className='col-sm-8 text-light'
                                ),                
                            html.Div(
                                html.Img(src="./assets/img/ds4a.png", style={'height': '30px', 'width': '100px'}),
                                className='col-sm-2'
                            ),
                            html.Div(
                                html.Img(src="./assets/img/mintic.png", style={'height': '30px', 'width': '100px'}),
                                className='col-sm-2'
                            )
                        ],                    
                        className='row bg-secondary'
                    ),                     
                    html.Nav(
                        html.Div(children=[
                        ##html.Div(html.A(html.Img(src="./assets/img/ds4a.png", sizes="30px"), href="/", className="navbar-brand")),
                        html.A(html.Img(src="./assets/img/logo 2.png", sizes="30px"), href="/", className="navbar-brand"),
                        html.Button( children=[
                            html.Span( className="navbar-toggler-icon")
                        ],
                        
                        type="button", className="navbar-toggler"
                                        
                        ),
                        html.Div(children=[
                            html.Ul(
                                children=[
                                    html.Li(
                                        html.A("Home", href="/home", className="nav-link active h5")
                                        , className="nav-item"),
                                    html.Li(
                                        html.A("Eda", href="/EDA", className="nav-link active h5")
                                        , className="nav-item"),
                                    html.Li( 
                                        html.A( "Analizer", href="/search", className="nav-link active h5")
                                        , className="nav-item" ),
                                    html.Li( 
                                        html.A("Graphs", href="/scatterplot", className="nav-link active h5")
                                        , className="nav-item")
                            ], className="ml-auto navbar-nav")
                        ], className="collapse navbar-collapse")
                        ], className="container"),
                        className="navbar navbar-expand-md navbar-light navbar-dark bg-primary"
                    )
                ],
                )
    return header

def get_menu():
    navbar = ""
    """ dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("EDA", href="/EDA")),
        dbc.NavItem(dbc.NavLink("Analizer", href="/search")),
        dbc.NavItem(dbc.NavLink("Scatterplot", href="/scatterplot"))
    ],
    brand="Twittycs.ml",
    brand_href="/",
    color="primary",
    dark=True,
    ) """
    return navbar

def get_footer():
    footer = html.Footer(
        html.Div("© 2021 Copyright: Twittycs.ml",
            className="text-center p-4"),
        className='text-center text-lg bg-secondary text-muted')   
    return footer

