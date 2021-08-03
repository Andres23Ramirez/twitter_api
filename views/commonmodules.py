import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from views import commonmodules

from app import app

def get_header():
    header = html.H1('DS4A - TEAM #54', className='text-center')
    return header

def get_menu():
    navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Line Chart", href="/linechart")),
        dbc.NavItem(dbc.NavLink("Bar Chart", href="/barchart")),
        dbc.NavItem(dbc.NavLink("Scatterplot", href="/scatterplot"))
    ],
    brand="Team #54",
    brand_href="/",
    color="primary",
    dark=True,
    )
    return navbar

def get_footer():
    footer = html.Footer(
        html.Div("© 2021 Copyright: Team #54",
            className="text-center p-4"),
        className='text-center text-lg-start bg-light text-muted')
        
    
    return footer

