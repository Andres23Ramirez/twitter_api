import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from views import commonmodules
import pandas as pd
from io import BytesIO
from wordcloud import WordCloud
import base64
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from stop_words import get_stop_words
from wordcloud import WordCloud
pd.set_option("display.max_colwidth",10)
warnings.filterwarnings("ignore",category=DeprecationWarning)
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from nltk.tokenize.regexp import regexp_tokenize
from plotly.subplots import make_subplots

from app import app

palabras_irrelevantes = get_stop_words('spanish')


datos2 = pd.read_csv('data/results.csv')
df = datos2.copy()
df = df.reset_index().drop(columns='index')
df.created_at = pd.to_datetime(df.created_at)

fig = px.histogram(df,
                    x = 'polarity',
                    marginal = 'rug', 
                    nbins= 20,
                    hover_data = ['full_text'],
                    log_y = True)

## Figura 2

hist_data = [df.polarity.to_numpy()]
group_labels = ['Polaridad'] # name of the dataset
bins = 0.05

fig2 = ff.create_distplot(hist_data, group_labels, bin_size=.1)
#fig2.update_layout(title_text = 'Polarity of the Tweets')

##figura 3

neg = -0.2
pos = 0.2
df['value'] = 'Neutral'
df.loc[df['polarity'] > pos, 'value'] = 'Positive'
df.loc[df['polarity'] < neg, 'value'] = 'Negative'



df.groupby('value')['polarity'].count().index
fig3 = px.pie(df.groupby('value')['polarity'].count(), 
            values = df.groupby('value')['polarity'].count(),
            names = df.groupby('value')['polarity'].count().index,
            color = df.groupby('value')['polarity'].count().index,
            color_discrete_map={'Neutral':'blue', 'Positive':'green', 'Negative':'red'})


##figura 4
df = pd.concat([df, pd.get_dummies(df.value)], axis = 1)
bucket = 4
ts = df[['created_at', 'Negative', 'Neutral', 'Positive']].resample(f'{bucket}H', on = 'created_at').sum()

fig4 = go.Figure()
fig4.add_trace(go.Scatter(x = ts.index, y = ts.Neutral , fill = 'tozeroy', mode='none', hoverinfo = 'x+y', name='Neutral',
line = dict(width = 0.5, color = 'rgb(114, 114, 114)')))
fig4.add_trace(go.Scatter(x = ts.index, y = ts.Negative, fill = 'tozeroy', mode='none', hoverinfo = 'x+y', name='Negative',
line = dict(width = 0.5, color = 'rgb(202,   0,  42)')))
fig4.add_trace(go.Scatter(x = ts.index, y = ts.Positive, fill = 'tonexty', mode='none', hoverinfo = 'x+y', name='Positive',
line = dict(width = 0.5, color = 'rgb( 69, 229,  33)')))

fig4.update_xaxes(rangeslider_visible = True)
fig4.update_layout(
    title = f"Sentiment evolution over time ({bucket} - hour bucket)",
    xaxis_title = "Time",
    yaxis_title = "Amount of tweets",
    legend_title = "Sentiment"
    ) 

#Figura 5
large = 1200
pos_textoWC = ' '.join(df.loc[df['value'] == 'Positive', 'clean_text'])
pos_wordcloud = WordCloud(width = large, height = large, 
                background_color ='white', 
                stopwords = palabras_irrelevantes,# max_words=200,
                relative_scaling = 0,
                min_font_size = 10).generate(pos_textoWC) 

neg_textoWC = ' '.join(df.loc[df['value'] == 'Negative', 'clean_text'])
neg_wordcloud = WordCloud(width = large, height = large, 
                background_color ='white', 
                stopwords = palabras_irrelevantes,# max_words=200,
                relative_scaling = 0,
                min_font_size = 10).generate(neg_textoWC) 

neu_textoWC = ' '.join(df.loc[df['value'] == 'Neutral', 'clean_text'])
neu_wordcloud = WordCloud(width = large, height =  large, 
                background_color ='white', 
                stopwords = palabras_irrelevantes,# max_words=200,
                relative_scaling = 0,
                min_font_size = 10).generate(neu_textoWC) 

plt.figure(figsize = (8, 8), facecolor = None) 
#fig5 = plt.subplots(1, 3)
#wc = WordCloud(background_color='black', width=480, height=360)
fig_pos_wordcloud = pos_wordcloud.to_image
fig_neu_wordcloud = neu_wordcloud.to_image
fig_neg_wordcloud = neg_wordcloud.to_image

""" ax1.axis("off")
ax1.set_title("Negative Tweets") 
ax2.imshow(neu_wordcloud, interpolation='bilinear')
ax2.axis("off")
ax2.set_title("Neutral Tweets")
ax3.imshow(pos_wordcloud, interpolation='bilinear')
ax3.axis("off")
ax3.set_title("Positive Tweets") 
plt.tight_layout(pad = 0) 
fig5.suptitle('Word Cloud of:')   """

##Figura 6
fig6 = px.histogram(df,
                    x = 'favorite_count', 
                    color = "value",  
                    marginal = "rug", 
                    hover_name = "full_text",
                    color_discrete_sequence = ['blue', 'red', 'green']
)
fig6.update_traces(opacity=0.75)
fig6.update_layout(barmode='overlay')
fig6.update_layout(
    xaxis_title = "Favourite count",
    yaxis_title = "Frequency",
    legend_title = "Sentiment"
    )

#Figura 7
fig7 = px.histogram(df,
                    x = 'retweet_count', 
                    color = "value",  
                    marginal = "rug", 
                    color_discrete_sequence = ['blue', 'red', 'green'],
                    # histnorm='probability density'
                    hover_name = "full_text",
)
fig7.update_traces(opacity=0.75)
fig7.update_layout(barmode='overlay')
fig7.update_layout(
    xaxis_title = "Retweet count",
    yaxis_title = "Frequency",
    legend_title = "Sentiment"
    )


df.groupby('value')[['retweet_count', 'favorite_count']].mean()
df['tweet'] = df['clean_text'].apply(lambda x:regexp_tokenize(x,pattern='\s+',gaps=True))
df2 = df.explode('tweet')

Positive = pd.DataFrame(df2.loc[df2['value'] == 'Positive', 'tweet'].value_counts())
Neutral = pd.DataFrame(df2.loc[df2['value'] == 'Neutral', 'tweet'].value_counts())
Negative = pd.DataFrame(df2.loc[df2['value'] == 'Negative', 'tweet'].value_counts())

Positive.reset_index(inplace = True)
Neutral.reset_index(inplace = True)
Negative.reset_index(inplace = True)

Positive = Positive[Positive['index'].str.len()>3]
Neutral = Neutral[Neutral['index'].str.len()>3]
Negative = Negative[Negative['index'].str.len()>3]

Positive['Sentiment'] = 'Positive'
Negative['Sentiment'] = 'Negative'

top = 15

funnel = pd.concat([Positive.iloc[:top], Negative.iloc[:top]])
funnel.columns = ['Word', 'Amount of tweets', 'Sentiment']
fig8 = px.funnel(funnel, x='Amount of tweets', y='Word', color='Sentiment',  color_discrete_sequence = ['green', 'red'])

fig9 = make_subplots(rows=1, cols=2, column_widths=[0.7, 0.3])

fig9.add_trace(go.Bar(x = Positive.loc[:top, 'tweet'],
                     y = Positive.loc[:top, 'index'],
                     orientation='h',
                     # color = ['green'],
                     name = 'Positive'),
              row = 1,
              col = 1
      #      color_discrete_sequence = ['green']
            )
fig9.update_layout(yaxis={'categoryorder':'total ascending'})
fig9.add_trace(go.Bar(x = Negative.loc[:top, 'tweet'],
                     y = Negative.loc[:top, 'index'],
                     orientation='h',
                     name = 'Negative'),
        #        color_discrete_sequence = ['red']
               row = 1,
               col = 2
             )
fig9.update_layout(yaxis={'categoryorder':'total ascending'})

fig10 = px.bar(x = Positive.loc[:top, 'tweet'],
             y = Positive.loc[:top, 'index'],
             # color_discrete_sequence = ['green'],
             orientation = 'h')
fig10.update_layout(yaxis={'categoryorder':'total ascending'})
fig10.update_layout(
    title = f"Words associated to positive sentiement",
    xaxis_title = "Tweet count",
    yaxis_title = "Words"
    )

fig11 = px.bar(x = Negative.loc[:top, 'tweet'],
             y = Negative.loc[:top, 'index'],
             # color_discrete_sequence = ['green'],
             orientation = 'h')
fig11.update_layout(yaxis={'categoryorder':'total ascending'})
fig11.update_layout(
    title = f"Words associated to negative sentiement",
    xaxis_title = "Tweet count",
    yaxis_title = "Words"
    )
##Figura 12 la del tiempo 
##--------------------------------------------
df = pd.concat([df, pd.get_dummies(df.value)], axis = 1)
bucket = 4
ts = df[['created_at', 'Negative', 'Neutral', 'Positive']].resample(f'{bucket}H', on = 'created_at').sum()
ts2 = pd.melt(ts.reset_index(), id_vars = ['created_at'], value_vars = ['Negative', 'Neutral', 'Positive'])
ts2.created_at = ts2.created_at.dt.strftime("%Y%m%d%H%M").str[:-2]
fig12 = px.bar(ts2, 
             x = "value", 
             y = "variable", 
             color = "variable",
             animation_frame = "created_at",
             range_x=[0,max(ts2.value)],
             labels = {'variable': 'Sentiment', 'value': 'Amount of tweets', 'created_at': 'time'},
             color_discrete_map={'Neutral':'blue', 'Positive':'green', 'Negative':'red'}
            )
##Layout --------------------------------------------

layout = html.Div([
    commonmodules.get_header(),
    commonmodules.get_menu(),
    dbc.Container([
        html.Br(),
        html.Br(),
        html.H1(
            "Now we focus on identifying the characterization of the tweets, so we can infer the drivers of a positive or negative tweet."
        , className='text-center font-weight-bold'),
        html.Div(
            dcc.Graph(figure=fig12),
            className="border"
        ),
        html.Br(),
        html.Br(),
        html.H2("WordCloud", className='text-center font-weight-bold'), 
        html.Div(
            html.Div([
                html.Div([
                    html.H3("Positive Tweets", className='text-center font-weight-bold'),
                    html.Img(id="fig_pos_wordcloud",
                    className = "img-fluid", alt=""
                    )
                ],
                    className="col-sm"
                ),
                html.Div([
                    html.H3("Neutral Tweets", className='text-center font-weight-bold'),
                    html.Img(id="fig_neu_wordcloud",
                    className = "img-fluid", alt=""
                    )
                ],
                    className="col-sm"
                ),
                html.Div([
                    html.H3("Negative Tweets", className='text-center font-weight-bold'),
                    html.Img(id="fig_neg_wordcloud",
                    className = "img-fluid", alt=""
                    )
                ],
                    className="col-sm"
                ),
                ],
                className="row"
            ),
            className="container"
        ),
        html.Br(),
        html.Br(),
        html.H2("Words associated to positive sentiement", className='text-center font-weight-bold'),
        html.Div(
            dcc.Graph(figure=fig10),
            className="border"
        ),
        html.H2("Words associated to negative sentiement", className='text-center font-weight-bold'),
        html.Div(
            dcc.Graph(figure=fig11),
            className="border"
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H2('Polarity of the Tweets', className='text-center font-weight-bold'),   
        html.Div(
            dcc.Graph(figure=fig),
            className="border"
        ),
        html.Br(),
        html.Br(),
        html.H2("Polarity of the Tweets", className='text-center font-weight-bold'),
        html.Div(
            dcc.Graph(figure=fig2),
            className="border"
        ),
        html.Br(),
        html.Br(),
        html.H2("PieChart Polarity of the Tweets", className='text-center font-weight-bold'),
        html.Div(
            dcc.Graph(figure=fig3),
            className="border"
        ),
        html.Br(),
        html.Br(),
        html.H2(f"Sentiment evolution over time ({bucket} - hour bucket)", className='text-center font-weight-bold'),
        html.Div(
            dcc.Graph(figure=fig4),
            className="border"
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H2('Likes distribution across the different sentiments', className='text-center font-weight-bold'),
        html.Div(
            dcc.Graph(figure=fig6),
            className="border"
        ),
        html.Br(),
        html.Br(),
        html.H2("Retweets distribution across the different sentiments", className='text-center font-weight-bold'),
        html.Div(
            dcc.Graph(figure=fig7),
            className="border"
        ),
        html.Br(),
        html.P('The previous plots show for the period of analisys that the neutral tweets are the most favored and retweeted, followed by the positive. Negative sentiment in the tweets seems not to be spread as the rest if the information. However, below we show the average values of the retweet count and favoroured count for each sentiment, where it is to emphasize that the "natural order of the catagories" seems to prevail. Nevertheless that pattern is not followed by the retweet, where the neutral tweets tend do lead the dissemination of information.'),
        html.Br(),
        html.H2("Amount of tweets", className='text-center font-weight-bold'),
        html.Div(
            dcc.Graph(figure=fig8),
            className="border"
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H2("category Order", className='text-center font-weight-bold'),
        html.Div(
            dcc.Graph(figure=fig9),
            className="border"
        )
                  
    ]),
    commonmodules.get_footer(),
])

def plot_wordcloud(data):
    return data.to_image()

@app.callback([Output('fig_pos_wordcloud', 'src'), 
               Output('fig_neu_wordcloud', 'src'), 
               Output('fig_neg_wordcloud', 'src')], 
              [Input('fig_pos_wordcloud', 'id'),
               Input('fig_neu_wordcloud', 'id'),
               Input('fig_neg_wordcloud', 'id')])
def make_image(a,b,c):
    img1 = BytesIO()
    img2 = BytesIO()
    img3 = BytesIO()
    plot_wordcloud(data=pos_wordcloud).save(img1, format='PNG')
    plot_wordcloud(data=neu_wordcloud).save(img2, format='PNG')
    plot_wordcloud(data=neg_wordcloud).save(img3, format='PNG')
    a = 'data:image/png;base64,{}'.format(base64.b64encode(img1.getvalue()).decode())
    b = 'data:image/png;base64,{}'.format(base64.b64encode(img2.getvalue()).decode())
    c = 'data:image/png;base64,{}'.format(base64.b64encode(img3.getvalue()).decode())
    return a, b, c
