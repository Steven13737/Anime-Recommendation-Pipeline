# Anime-Recommendation-Pipeline

# Start
```python
python web.py
python preict_server.py # in another terminal
```

# Dependency 
+ kafka-python
+ pymysql
+ tornado

# Service
+ Identity Verification Service
+ Recommendation Service
  + CF Recommendation 
  + Content-Based Recommendation
  
# Framework
+ Front-end: Ajax 
+ Back-end: Tornado
+ Messgae queue: Kafka
+ Database: mysql

# Directory
|-- kafka: show an simple example for how to send and receive message and control offset\
|-- PredictService: predict cf based recommendation \
|-- web.py: Tornado main server file


