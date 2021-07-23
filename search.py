# Import the Twython class
from twython import Twython
import json
import pandas as pd
import csv

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# Instantiate an object
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

# Create our query
query = {'q': 'pfizer ',
        'result_type': 'mixed',
        'count': 100,
        'lang': 'es',
        'geocode': {"4.6762539246186385", "-74.11467451254052","50km" },
        'tweet_mode': 'extended'
        }

statuses = python_tweets.search(**query)['statuses']

mayor = 0
index = 0
for x in statuses:
    if len(x) > mayor:
        mayor = len(x)
        index = statuses.index(x)

#myheaders = statuses[index].keys()
#myheaders = ['extended_entities', 'retweeted_status', 'created_at', 'id', 'id_str','full_text', 'text', 'truncated', 'entities', 'metadata', 'source', 'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'in_reply_to_screen_name', 'user', 'geo', 'coordinates', 'place', 'contributors', 'is_quote_status', 'quoted_status_id', 'quoted_status_id_str', 'quoted_status', 'retweet_count', 'favorite_count', 'favorited', 'retweeted', 'possibly_sensitive', 'lang']
myheaders = ['created_at', 'id', 'id_str','full_text', 'source','truncated','in_reply_to_status_id','in_reply_to_status_id_str','in_reply_to_user_id','in_reply_to_user_id_str','in_reply_to_screen_name','user','coordinates','place','quoted_status_id','quoted_status_id_str','is_quote_status','quoted_status','retweeted_status','quote_count','reply_count','retweet_count','favorite_count','entities','extended_entities','favorited','retweeted','possibly_sensitive','filter_level','lang','matching_rules', 'current_user_retweet', 'scopes', 'withheld_copyright', 'withheld_in_countries', 'withheld_scope', 'contributors', 'geo', 'metadata', 'display_text_range']

with open('tweets_result2.csv', 'w', newline='') as myfile:    
    writer = csv.DictWriter(myfile, fieldnames=myheaders)
    writer.writeheader()
    writer.writerows(statuses) 
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