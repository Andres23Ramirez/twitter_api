import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from views import barchart, barchart, commonmodules

from app import app
team_mates = ['Valentina Parra', 'Rodian Andrés Oliveros', 'Edwin Romero', 'David Mauricio Arquez', 'Felipe Bonnet', 'Oscar Andrés Zapata', 'Rodrigo Andrés Ramírez Aguirre' ]

layout = html.Div([
    commonmodules.get_header(),
    commonmodules.get_menu(),
    html.Br(),
    html.H2('Cracking the code: In uncertain times, who do we trust? A sentiment analysis of the COVID-19 vaccines perception in Colombia'),
    html.Br(),
    html.H3('Team Members'),
    html.Div(
        className="team_mates",
        children=[
            html.Ul(id='team_mates', children=[html.Li(i) for i in team_mates])
        ],
    ),
    html.Br(),
    html.H3('Executive Summary'),
    html.P('History is written by the victors, and we as humans have been told what the truth is from an unanimous source we haven’t truly questioned. Yet, in these trying times filled with uncertainty and fear, a lack of trust over the truth has reigned over us, preventing us from taking informed decisions. Polarization has spiked thanks to an incessant barrage of news declaring each piece as the sole owner of the “truth”, leading to paralysis in the face of decision-making.'),
    html.P('This phenomenon has been affecting us for quite some time, but never has it been more prevalent than during the COVID-19 pandemic. Social media and technology have facilitated the spread of (mis)communication, leading to easy access to “reputable” sources claiming the truth behind the source of the virus, the efficacy of quarantine measures, and the safety of the vaccines, amongst many others.'),
    html.P('For all governments, it is essential that their population understands the pandemic and how vaccination can be a powerful weapon against it. To date, Colombia has managed to vaccinate nearly 30% of its population, as well as opening it’s vaccination efforts to all the general population, having previously been restricted to the older and vulnerable age groups. Nonetheless, it is still facing constant backlash and outright refusal from opposers who do not trust the safety of the process nor the intentions of the government.'),
    html.P('Herein lies the crux of the matter: ¿How can the Colombian government support and improve its vaccination efforts? This question leads the investigative, analytical, and conclusive endeavor of this project, geared towards the Ministerio de Salud and their potential measures towards increasing vaccination rate.'),

    html.Br(),
    html.H3('Business Context'),
    html.P('Colombia has had roughly 33% of the population vaccinated with at least one dosis against COVID-19, though it lags behind some of its south american neighbours who already have over 50% of their population partly vaccinated. In the graph below, we can identify that Colombia occupies the 6 position out of the 12 South American countries, evidencing the reduced pacing the country faces (Mathieu, Ritchie, Ospina et al, 2021). '),
    html.Div([ 
            html.Img(
                    src = app.get_asset_url('img/coronavirus-data-explorer.png'),
                    height = '75%',
                    width = '75%')
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
    html.P('The results of the survey can be shown in the graph below, with one being the least and five being the most important reason why a physician would accept a free vaccine (Basel, 2021).'),
    html.Div([ 
            html.Img(
                    src = app.get_asset_url('img/effectiveness.jpg'),
                    height = '75%',
                    width = '75%')
            ],
            className = '',
            style = {
                    'alignItems': 'center',
                    'paddingTop' : '1%',
                    'height' : '95%',
                    'width' : '95%'}),
    html.P('According to the conclusions of this study, it was found that between 77% and 90,7% of surveyed physicians accepted Colombia’s COVID-19 vaccination. While these results are encouraging, and despite the rather favourable reception, the same conclusion may not apply to the general population. '),
    html.P('Comprehending the digital media landscape and identifying one of the most used and influential networks for news sharing and commenting led to the subsequent analysis of Twitter. Aiming to further understand the perception of the general public, this study tried to analyze the comments surrounding the different vaccines in Twitter, one of the countries most used social media amongst digital users (Statista, 2021).'),
    html.Div([ 
            html.Img(
                    src = app.get_asset_url('img/statista.png'),
                    height = '75%',
                    width = '75%')
            ],
            className = '',
            style = {
                    'alignItems': 'center',
                    'paddingTop' : '1%',
                    'height' : '95%',
                    'width' : '95%'}),
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
    html.P("Which will allow us to predict how the immunity process will be and at what speed the contagion curve can be reduced in Colombia by knowing what the perception of people regarding vaccination is and if they are willing to do so, these results can be of great useful for the government to carry out programs that encourage vaccination and show evidence so that people can make the best decision whether to get vaccinated or not.")

])