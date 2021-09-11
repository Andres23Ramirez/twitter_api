import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from pkg_resources import yield_lines
from views import commonmodules

from app import app
team_mates = {'Valentina Parra Garces': "https://www.linkedin.com/in/vparrag", 
              'Rodian Andrés Oliveros': 'https://www.linkedin.com/in/rodianoliveros/', 
              'Edwin Romero Cuero': "", 
              'David Mauricio Arquez': "", 
              'Felipe Bonnet': "https://www.linkedin.com/in/felipe-bonnet", 
              'Oscar Andrés Zapata': "", 
              'Rodrigo Andrés Ramírez Aguirre': "https://www.linkedin.com/in/rodrigo-andres-ramirez-aguirre-b1aa20126/" }

layout = html.Div([
    commonmodules.get_header(),
    commonmodules.get_menu(), 
    dbc.Carousel(
            items=[
                {
                    "key": "1",
                    "src": "/assets/img/2.png",
                    "header": "Twittycs - A sentiment analysis of the COVID-19 vaccines perception in Colombia"
                },
                {
                    "key": "2",
                    "src": "/assets/img/3.png",
                    "header": "Vaccines save lives, let's find out what Twitter has to say"
                },
                {
                    "key": "3",
                    "src": "/assets/img/5.png",
                    "header": "In uncertain times, who do we trust? "
                },
            ],
            indicators=False
        ),   
    dbc.Container([        
        html.Br(),
        html.Br(),
        html.Br(),
        html.H2('Cracking the code: In uncertain times, who do we trust?', className='text-center font-weight-bold'),
        html.P('A sentiment analysis of the COVID-19 vaccines perception in Colombia', className='text-center font-italic'),
        html.Br(),
        html.Hr(),
        html.Br(),
        html.Br(),
        html.H2('Summary', className='text-center font-weight-bold'),
        html.Br(),
        html.Br(),
        html.Div(children=[
                html.Iframe( "allowfullscreen"
                    ,className="embed-responsive-item" 
                    ,src="https://www.youtube.com/embed/0NlGDhjNrzY" 
                )]
            ,className="embed-responsive embed-responsive-4by3"
        ),
        html.Br(),
        html.Hr(),
        html.H2('Team Members', className='text-center font-weight-bold'),
        html.Br(),
        html.Br(),
        html.H3("Members: "),
        html.Div(children=[ 
            html.Div(children=[
                html.Div(children=[
                        html.Div(
                            className="team_mates",
                            children=[
                                html.Ul(id='team_mates', children=[html.Li(children=[html.H3(key), html.A("Linkedin", href=value)]) for key, value in team_mates.items()])
                            ],
                    ),
                    ], className='col-sm-6'),
                    html.Div(children=[
                        dbc.Carousel(
                                items=[
                                    {
                                        "key": "1",
                                        "src": "/assets/img/valentina.png",
                                        "header": "Valentina Parra Garces",
                                        "caption": "Data Scientist and Machine Learning Engineer",
                                        "imgClassName": "image_new_class"
                                    },
                                    {
                                        "key": "2",
                                        "src": "/assets/img/rodian.png",
                                        "header": "Rodian Andrés Oliveros",
                                        "caption": "Data Analyst / Data Scientist",
                                        "imgClassName": "image_new_class"
                                    },
                                    {
                                        "key": "3",
                                        "src": "/assets/img/felipe.png",
                                        "header": "Felipe Bonnet",
                                        "caption": "Director, cinematographer and Data Translator",
                                        "imgClassName": "image_new_class"
                                    },
                                    {
                                        "key": "4",
                                        "src": "/assets/img/edwin.jpg",
                                        "header": "Edwin Romero Cuero",
                                        "caption": "Data Scientist and Machine Learning Engineer",
                                        "imgClassName": "image_new_class"
                                    },
                                    {
                                        "key": "5",
                                        "src": "/assets/img/not_photo.png",
                                        "header": "David Mauricio Arquez",
                                        "caption": "designer, Data Translator and BI",
                                        "imgClassName": "image_new_class"
                                    },
                                    {
                                        "key": "6",
                                        "src": "/assets/img/not_photo.png",
                                        "header": "Oscar Andrés Zapata",
                                        "caption": "Data Engineer",
                                        "imgClassName": "image_new_class"
                                    },
                                    {
                                        "key": "7",
                                        "src": "/assets/img/rodrigo.png",
                                        "header": "Rodrigo Andres Ramirez Aguirre",
                                        "caption": "Developer Expert and Data Engineer",
                                        "imgClassName": "image_new_class"
                                    },
                                ],
                                indicators=False,
                                className='carousel-fade carousel-thumbnails'
                            ), 
                    ], className='col-sm-6 '),
                ], className='row'),
            ], className='container'),
        html.Br(),
        html.Br(),
        html.Hr(),
        html.H3('Business Context', className='text-center font-weight-bold'),
        html.P('Colombia has had roughly 33% of the population vaccinated with at least one dosis against COVID-19, though it lags behind some of its south american neighbours who already have over 50% of their population partly vaccinated. In the graph below, we can identify that Colombia occupies the 6 position out of the 12 South American countries, evidencing the reduced pacing the country faces (Mathieu, Ritchie, Ospina et al, 2021). '),
        html.Div([ 
                html.Img(
                        src = app.get_asset_url('img/coronavirus-data-explorer.png'),
                        height = '75%',
                        width = '75%',
                        style = {
                        'alignItems': 'center',
                        'paddingTop' : '1%',
                        'height' : '95%',
                        'width' : '95%'})
                ],
                className = '',
                style = {
                        'alignItems': 'center',
                        'paddingTop' : '1%',
                        'height' : '95%',
                        'width' : '95%'}),
        html.P('According to a survey directed towards medical staff conducted by researchers of the National Center for Biotechnology Information, the main reasons for vaccination are as follows:'),
        html.Div(
            children=[
                html.Ol(children=[html.Li(i) for i in [
                    'Personal protection to avoid getting sick',
                    'Protection of my close relatives',
                    'Getting vaccinated it most convenient for everyone',
                    'Is the best public health strategy in the pandemic',
                    'There are no other options at the moment to prevent getting sick'
                ]])
            ],
        ),
        html.Hr(),

        html.P("Team 54 wants to apply several of the tools seen during the DS4A Colombia program to be able to carry out a sentiment analysis through the NLP (Natural Language Processing) technique through the Twitter developer tool in order to extract data and understand what is the People's perception regarding a conjunctural issue such as vaccination in times of the Pandemic (COVID-19) and being able to understand this reality in Colombia and share the findings using Data Science."),
        html.P("The vaccination panorama in Colombia lags behind its Latin American peers, but the government's vaccination programs are advancing to be able to carry out this objective in stages where vaccination is being carried out by age range, while people are also adopting new ones behaviors and ways of thinking in society with respect to this reality."),
        html.P("Therefore, it is important to analyze what the impression is and how people are assimilating this, for this we want to tear data from the people who post tweets regarding vaccines, having as an axis the tweets that contain keywords such as the names of the vaccines, pandemic, COVID-19 and understand if there are clusters where the perception is negative or positive."),
        html.P("This is important to be able to move forward in this new reality and provide understanding on an issue where myths and fake news can skew the ideal and the thinking of society."),
        html.P("The expected results of the project are:"),
        html.Div(
            children=[
                html.Ul(children=[html.Li(i) for i in [
                    'Understand the perception of people regarding the vaccination against COVID 19 through a sample of the opinions of twitter, a social network that is characterized by its freedom of expression.',
                    'Predict the evolution of vaccination and the contagion curve with respect to the willingness of people to be vaccinated or not.'
                ]])
            ],
        ),
        html.P("Which will allow us to predict how the immunity process will be and at what speed the contagion curve can be reduced in Colombia by knowing what the perception of people regarding vaccination is and if they are willing to do so, these results can be of great useful for the government to carry out programs that encourage vaccination and show evidence so that people can make the best decision whether to get vaccinated or not."),
        ]),
    commonmodules.get_footer(),
    ])