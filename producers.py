import tweepy
import time
from datetime import timedelta
from kafka import KafkaConsumer, KafkaProducer, consumer

#twitter setup
consumer_key = "57UfXTOkbyTwgSLw6BTAjinag"
consumer_secret = "f3JwlqA7etSNgFAUe5FWoX4sx85YKwazHusZlS6eGMU6jfqsvr"
access_token = "1264503941061988352-niF9CQvaB46c2p14YfIn1q346fkXQW"
access_token_secret = "4KwPkRTbiwVdSTHGSwCOMBlZtYJPSDYsxcNbGD3xpNeXt"

#creating the authenctication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

#setting access token
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

from datetime import datetime

def normalize_timestamp(time):
    mytime = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    return (mytime.strftime("%Y-%m-%d %H:%M:%S"))

producer = KafkaProducer(bootstrap_servers = 'localhost:9092')
topic_name = 'steam'

#get Data
def get_twitter_data():
    res = api.search('steam')
    count = 1
    for i in res:
        record = ''
        record += str(i.user.id_str)
        record += '~'
        record += str(i.text)
        record += '~'
        record += str(normalize_timestamp(str(i.created_at)))
        record += '~'
        print("get ", count, " tweet")
        producer.send(topic_name, str.encode(record))
        count += 1

def periodic_work(interval):
    while True:
        get_twitter_data()
        time.sleep(interval)

periodic_work(5*1)