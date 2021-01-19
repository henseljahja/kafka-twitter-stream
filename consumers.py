from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import * 
from kafka import KafkaConsumer, consumer
import re
import time

#The ETL Process 
def etl_proses():
    customer = KafkaConsumer(bootstrap_servers = ['localhost:9092'], api_version=(0,10))
    customer.subscribe('<your topic_name>')

    tweet = []
    max = 0
    for message in customer:
        if max <= 20:
            tweet.append(message)
        else:
            break
        max += 1
        print("Read ",max, " tweet")

    cleansing = [re.sub("b'","", str(i.value)) for i in tweet]
    tweets = [i.split('~') for i in cleansing]

    #schema
    engine = create_engine('mysql+mysqlconnector://root:@localhost/steam')
    Base = declarative_base()

    class Users (Base):
        __tablename__ = "<your topic_name>"
        index = Column(Integer, primary_key = True)
        ids = Column(String(1000))
        tweet = Column(String(1000))
        date = Column(String(1000))

    Users.__table__.create(bind = engine, checkfirst = True)

    #Transform
    tweet = []
    index = 0
    for i in tweets:
        row = {}
        row['index'] = index
        row['ids'] = i[0]
        row['tweet'] = i[1]
        row['date'] = i[2]
        tweet.append(row)

    #load
    Session = sessionmaker(bind = engine)
    session = Session()

    for index in tweet:
        row = Users(**index)
        session.add(row)

    session.commit()
    session.close()


def periodic_work(interval):
    while True:
        etl_proses()
        time.sleep(interval)

periodic_work(2*1)