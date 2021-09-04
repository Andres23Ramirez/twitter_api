### A sentiment analysis of the COVID-19 vaccines perception in Colombia

This is a team 54's final project to DS4A / Colombia - Cohort 5.

**Team Members**
1.  Valentina Parra    
2.  Rodian Andrés Oliveros    
3.  Edwin Romero Cuero
4.  David Mauricio Arquez    
5.  Felipe Bonnet
6.  Oscar Andrés Zapata
7.  Rodrigo Andrés Ramirez 

This application is built in Python with the Flask framework and DASH.
It connects to the public Twitter API and dynamically retrieves tweets by passing it the name of a city and a list of words of the topic you want to analyze. We call this function "Analizer".

It has two sentiment analysis models which categorize tweets according to the text, into positive, neutral or negative. We call this function "Graphs".

In addition, we retrieved 10,000 tweets from the tweet API over a period of time, and performed sentiment analysis on the text of those tweets. We call this function EDA.

The application is running in: http://twittycs.ml:8050/

If you want to run in localhost, you need these:

## Pre-requisites

Have **Python3** installed

run: `pip install -r requirements.txt` 
run:  `python3 ./search.py`

## Code:

```
TWIITER_API
│   README.md
│   app.py
│   index.py
│   requirements.txt    
└───assets   
└───data
└───models
└───utilities
└───views
```
**index.js:**  Create the server and initialize the application 
**data:**  contains all the datasets that were used in the development of the project
**Models:** It contains the two sentiment analysis models that were carried out in the development of the project.
**utilities:** Contains functionalities that are used to perform a specific function in the application, such as downloading tweets, generating twitter api connection credentials, etc.
**Views:** It contains the views where the different datasets are plotted, the home page and the functionality to retrieve tweets from the public twetter api.