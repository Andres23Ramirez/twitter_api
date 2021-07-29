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

if os.path.isfile('data/tweets.csv'):
    exits = True
    df = pd.read_csv('data/tweets.csv')
    users = df[['user']]

    myheaders = ['id_user_tweet', 'id', 'id_str', 'name', 'screen_name', 'location', 'derived', 'url', 'description', 'protected', 'verified', 'followers_count', 'friends_count', 'listed_count', 'favourites_count', 'statuses_count', 'created_at', 'profile_banner_url', 'profile_image_url_https', 'default_profile', 'default_profile_image', 'withheld_in_countries', 'withheld_scope', 'geo_enabled', 'profile_sidebar_fill_color', 'profile_sidebar_border_color', 'following', 'is_translator', 'blocking', 'muting', 'lang', 'time_zone', 'profile_use_background_image', 'profile_background_image_url', 'follow_request_sent', 'profile_background_tile', 'profile_background_image_url_https', 'notifications', 'profile_text_color', 'profile_link_color', 'entities', 'is_translation_enabled', 'utc_offset', 'blocked_by', 'has_extended_profile', 'status', 'contributors_enabled', 'profile_image_url', 'translator_type', 'profile_background_color']

    if os.path.isfile('data/followers.csv'):
        exits = True
    else:
        exits = False
    
    if os.path.isfile('data/friends.csv'):
        exits_1 = True
    else:
        exits_1 = False


    for user in users['user']:
        if "," in user:
            id_user = user[7:user.index(",")]
            print(id_user)
                        
            followers = python_tweets.get_followers_list(id = id_user, count = 200)['users']
            
            for follow in followers:
                follow['id_user_tweet'] = id_user
                
            
            with open('data/followers.csv', 'a', newline='') as myfile:    
                writer = csv.DictWriter(myfile, fieldnames=myheaders)
                if not exits:
                    writer.writeheader()
                    exits = True
                writer.writerows(followers)

            time.sleep(70) 

            friends = python_tweets.get_friends_list(id = id_user, count = 200)['users']
            
            for friend in friends:
                friend['id_user_tweet'] = id_user
                
            
            with open('data/friends.csv', 'a', newline='') as myfile:    
                writer = csv.DictWriter(myfile, fieldnames=myheaders)
                if not exits_1:
                    writer.writeheader()
                    exits_1 = True
                writer.writerows(friends)

            time.sleep(70)
