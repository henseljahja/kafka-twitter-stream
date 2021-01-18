# kafka-twitter-stream
Full explanation how to stream twitter data by keyword, using kafka and python on Windows
# Installation & Setup guide

1. Download Java Development Kit 8 from [**Oracle Website**](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html), and install it
2. Download Apache Kafka from [**Apache Kafka Website**](https://kafka.apache.org/downloads), and set it up at ```C:/``` directory
3. Edit environment variable, and add ```C:\<Your Kafka Version>\bin\windows```
4. Add 2 folder named Kafka and Zookeper at ```C:\<Your Kafka Version\data\kafka``` and at ```C:\<Your Kafka Version\data\zookeeper``` 
5. Edit the Zookeper Configs File at ```C:\<Your Kafka Version>\config\zookeeper.properties``` and search for ```dataDir``` and edit it to ```C:/kafka_2.13-2.6.0/data/zookeeper```
6. Edit the Server Properties File at ```‪C:\kafka_2.13-2.6.0\config\server.properties``` and search for ```log.dirs``` and change it to ```log.dirs=C:/<Your kafka Version>/data/kafka```
# Starting the kafka client
```
git clone --recursive -j8 https://github.com/TelegramMessenger/Telegram-iOS.git
```
