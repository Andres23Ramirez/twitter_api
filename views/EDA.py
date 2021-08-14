import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from views import commonmodules
import pandas as pd
import dash_pivottable

df = pd.read_csv('data/tweets_mejorado 2.csv')
df = df.filter(["id","created_at", "coordinates", "place", "quote_count", "reply_count", "retweet_count",	"favorite_count",
	            "favorited", "retweeted",	"possibly_sensitive",	"filter_level",	"current_user_retweet", "display_text_range"])

from app import app
df2 = df[:5]
print(len(df2))

layout = html.Div([
    commonmodules.get_header(),
    commonmodules.get_menu(),   
    html.Div(
        dash_pivottable.PivotTable(
            data= df.values.tolist(),
            cols=["reply_count"],
            rows=df2["id"],
            vals=["Count"]
        ), 
        className='container'
    ),
    commonmodules.get_footer(),   
])