# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 18:55:33 2021

@author: alexandre
"""

import tweepy
import json 
import numpy as np
import pandas as pd
import twit_auth

tws=[]

i = 1
for tweet in tweepy.Cursor(api.search, q='skate', tweet_mode="extended",wait_on_rate_limit=True).items(1000000):
    tws.append(tweet) 
    print(i)
    i = i + 1
    
"""
what to save :
    date,
    twt,
    user_id,
    user_name,
    full_tweet,
    country/language,
"""
print(twt._json)
df =[]
for twt in tws:
    df.append({'twt_id': twt.id_str,
               'date': twt.created_at,
               'full_text': twt.full_text,
               'usr_name': twt.user.screen_name,
               'usr_id': twt.user.id_str,
               'lang': twt.lang,
               'location': twt.user.location,
               'description': twt.user.description})
    
df = pd.DataFrame(df)
df.drop_duplicates(subset="twt_id", keep='first', inplace=True)

df.to_csv('df.csv', index=False)

