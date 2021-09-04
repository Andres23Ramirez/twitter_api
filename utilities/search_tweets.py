# Import the Twython class
from twython import Twython
import json
import pandas as pd
import csv

def get_tweets(words, city, result_type, times):    
    # Load credentials from json file
    with open("twitter_credentials.json", "r") as file:
        creds = json.load(file)

    # Instantiate an object
    python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
    query_word = " OR ".join(words)
    query_word = city + " " + query_word
    min = 99999999999999999999

    # Create our query
    myheaders = ['created_at', 'id', 'id_str','full_text', 'source','truncated','in_reply_to_status_id','in_reply_to_status_id_str','in_reply_to_user_id','in_reply_to_user_id_str','in_reply_to_screen_name','user','coordinates','place','quoted_status_id','quoted_status_id_str','is_quote_status','quoted_status','retweeted_status','quote_count','reply_count','retweet_count','favorite_count','entities','extended_entities','favorited','retweeted','possibly_sensitive','filter_level','lang','matching_rules', 'current_user_retweet', 'scopes', 'withheld_copyright', 'withheld_in_countries', 'withheld_scope', 'contributors', 'geo', 'metadata', 'display_text_range']

    with open("tweets_analizer.csv", 'r+') as f:
        f.truncate(0)
        exist = False 

    query = {'q': query_word,
        'result_type': result_type, 
        'count': 100,
        'lang': 'es',
        'tweet_mode': 'extended'
        }

    for i in range(0, times, 1):        
        statuses = python_tweets.search(**query)['statuses']    
        with open('tweets_analizer.csv', 'a', newline='') as myfile:    
            writer = csv.DictWriter(myfile, fieldnames=myheaders)
            if not exist:
                writer.writeheader()
                exist = True
            writer.writerows(statuses) 
            myfile.close()            

        for status in statuses:     
            if min + 1 > status['id']:
                min = status['id']               
        
        query = {'q': query_word,
            'result_type': result_type,
            'count': 100,
            'lang': 'es',
            'tweet_mode': 'extended',
            'max_id': min
            }
    return pd.read_csv('tweets_analizer.csv')
