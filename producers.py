import tweepy
import time
from datetime import timedelta
from kafka import KafkaConsumer, KafkaProducer, consumer

consumer_key = "<Your Consumer Keys>"
consumer_secret = "<Your secret consumer keys>"
access_token = "<Your access token>"
access_token_secret = "<Your secret access token>"

#creating the authenctication object
#Creating the authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

#Setting the access token
auth.set_access_token(access_token, access_token_secret)

#Setup the API with the authentication
api = tweepy.API(auth)
#Importing datetime for the data stream
from datetime import datetime
#Normalizing the incoming datatime
def normalize_timestamp(time):
    mytime = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    return (mytime.strftime("%Y-%m-%d %H:%M:%S"))
#setup the producers, to the local host that has been defined in the kafka consumer
producer = KafkaProducer(bootstrap_servers = 'localhost:9092')
#the topic name that has been setup from the shell
#kafka-topics.bat --zookeeper localhost:2181 --create –topic <topic_name> --partitions <Number of Partitions> --replication-factor 1

topic_name = '<topic_name>'

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
#Counting the interval from which you stream the data
def periodic_work(interval):
    while True:
        get_twitter_data()
        time.sleep(interval)

periodic_work(5*1)