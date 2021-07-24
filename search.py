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
words = ["pfizer", "sinovac", "astrazenea", "janssen", "vacuna"]
query_word = " OR ".join(words)
min = 0

# Create our query
query = {'q': query_word,
        'result_type': 'mixed',
        'count': 100,
        'lang': 'es',
        'geocode': {"4.6762539246186385", "-74.11467451254052","700km" },
        'tweet_mode': 'extended'
        }

myheaders = ['created_at', 'id', 'id_str','full_text', 'source','truncated','in_reply_to_status_id','in_reply_to_status_id_str','in_reply_to_user_id','in_reply_to_user_id_str','in_reply_to_screen_name','user','coordinates','place','quoted_status_id','quoted_status_id_str','is_quote_status','quoted_status','retweeted_status','quote_count','reply_count','retweet_count','favorite_count','entities','extended_entities','favorited','retweeted','possibly_sensitive','filter_level','lang','matching_rules', 'current_user_retweet', 'scopes', 'withheld_copyright', 'withheld_in_countries', 'withheld_scope', 'contributors', 'geo', 'metadata', 'display_text_range']

if os.path.isfile('tweets.csv'):
    exits = True
else:
    exits = False

for i in range(0, 100, 1):

    statuses = python_tweets.search(**query)['statuses']

    with open('tweets.csv', 'a', newline='') as myfile:    
        writer = csv.DictWriter(myfile, fieldnames=myheaders)
        if not exits:
            writer.writeheader()
        writer.writerows(statuses) 

    for status in statuses:
        if min < status['id']:
            min = status['id']
    
    query = {'q': query_word,
        'result_type': 'mixed',
        'count': 100,
        'lang': 'es',
        'geocode': {"4.6762539246186385", "-74.11467451254052","700km" },
        'tweet_mode': 'extended',
        'max_id': min
        }
    
    time.sleep(10)
    print(i)

# Search tweets
""" dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
print(df) """