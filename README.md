# kafka-twitter-stream
Full explanation how to stream twitter data by keyword, using kafka and python on Windows
## Installation & Setup guide
### 1. Kafka Instalation
  1. Download Java Development Kit 8 from [**Oracle Website**](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html), and install it
  2. Download Apache Kafka from [**Apache Kafka Website**](https://kafka.apache.org/downloads), and set it up at ```C:/``` directory
  3. Edit environment variable, and add ```C:\<Your Kafka Version>\bin\windows```
  4. Add 2 folder named Kafka and Zookeper at ```C:\<Your Kafka Version\data\kafka``` and at ```C:\<Your Kafka Version\data\zookeeper``` 
  5. Edit the Zookeper Configs File at ```C:\<Your Kafka Version>\config\zookeeper.properties``` and search for ```dataDir``` and edit it to ```C:/kafka_2.13-2.6.0/data/zookeeper```
  6. Edit the Server Properties File at ```‪C:\kafka_2.13-2.6.0\config\server.properties``` and search for ```log.dirs``` and change it to ```log.dirs=C:/<Your kafka Version>/data/kafka```
### 2. Apply the [**Twitter Developers Account**](https://developer.twitter.com/en/apply-for-access), to get the API Keys
### 3. Download  [**XAMPP**](https://www.apachefriends.org/download.html) or [**MySQL Workbench**](https://dev.mysql.com/downloads/) to view the database
### 4. Starting & Creating kafka topics
  1. Open cmd at the directory instalation of zookeper and input
   ```zookeeper-server-start.bat config\zookeeper.properties``` 
  2. Open another cmd & run Kafka by typing
  ```kafka-server-start.bat config\server.properties```
  3. Create kafka topics by typing
   ```kafka-topics.bat --zookeeper localhost:2181 --create –topic <topic_name> --partitions <numbers_of_partition> --replication-factor 3```
  4. Run 
  ```python producers.py```
  5. Run 
  ```python consumers.py```
  6. Check MySql database, if enough data is collected, dump the etl by running
  ```python dump.py```
