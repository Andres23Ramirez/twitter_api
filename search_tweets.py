# Import the Twython class
from twython import Twython
import json
import pandas as pd
import csv
import os.path
import time

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
words = ["pfizer", "sinovac", "astrazenea", "janssen", "vacuna", "vacunacion"]
query_word = " OR ".join(words)
query_word = "Colombia AND " + query_word
min = 99999999999999999999
#min = 0


# Create our query
myheaders = ['created_at', 'id', 'id_str','full_text', 'source','truncated','in_reply_to_status_id','in_reply_to_status_id_str','in_reply_to_user_id','in_reply_to_user_id_str','in_reply_to_screen_name','user','coordinates','place','quoted_status_id','quoted_status_id_str','is_quote_status','quoted_status','retweeted_status','quote_count','reply_count','retweet_count','favorite_count','entities','extended_entities','favorited','retweeted','possibly_sensitive','filter_level','lang','matching_rules', 'current_user_retweet', 'scopes', 'withheld_copyright', 'withheld_in_countries', 'withheld_scope', 'contributors', 'geo', 'metadata', 'display_text_range']

if os.path.isfile('tweets_mejorado.csv'):
    exits = True
    df = pd.read_csv('tweets_mejorado.csv')
    min = df['id'].min()
    min = min - 1
    print("File exist: ")
    print(min)
    query = {'q': query_word,
        'result_type': 'mixed',
        'count': 100,
        'lang': 'es',
        'tweet_mode': 'extended',
        'max_id': min
        }    
else:
    exits = False
    query = {'q': query_word,
        'result_type': 'mixed', 
        'count': 100,
        'lang': 'es',
        'tweet_mode': 'extended'
        }

for i in range(0, 100, 1):
    print(i)
    print("-------------------------------------------")
    print("Query: " + str(query))
    statuses = python_tweets.search(**query)['statuses']
    print("Len: " + str(len(statuses)))
    time.sleep(10)
    with open('tweets_mejorado.csv', 'a', newline='') as myfile:    
        writer = csv.DictWriter(myfile, fieldnames=myheaders)
        if not exits:
            writer.writeheader()
            exits = True
        writer.writerows(statuses) 

    for status in statuses:     
        if min + 1 > status['id']:
            print("cambiando")
            print("min:    " + str(min))
            print("Status: " + str(status['id']))
            print("Resta: " + str(status['id'] - min))  
            min = status['id']
                    
            
    print("For min: ")
    print(min)
    
    query = {'q': query_word,
        'result_type': 'mixed',
        'count': 100,
        'lang': 'es',
        'tweet_mode': 'extended',
        'max_id': min
        }
