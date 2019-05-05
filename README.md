# Anime-Recommendation-Pipeline
Project for Data Pipeline

# Objective and MVP Overview
![System Framework](https://github.com/Steven13737/Anime-Recommendation-Pipeline/blob/master/src/Pipeline%20Service.png)
+ Online Recommendation service based on Collaborative filtering (CF) and content
+ Decouple the services through Kafka message queue to avoid synchronization and blocking
+ Offline training service for Collaborative filtering (CF) based on users' behaviour 
+ Identity verification service for login and recommendation
+ Database service for storage data

# How to Start
```python
python web/back-end/web.py

# In another terminal
python web/back-end/PredictServic/predict_service.py
```

# Dependency and Components
+ Python Packages:
  + Python 3.7
  + Tornado
  + kafka-python
  + pymysql
  + scikit-learn
+ Database: mysql
+ Message Queue: Kafka
+ Front-end: Ajax

# Walkthrough
![Walkthrough](https://github.com/Steven13737/Anime-Recommendation-Pipeline/blob/master/src/Logic.png)


# Database
[Details for database](https://github.com/Steven13737/Anime-Recommendation-Pipeline/tree/master/database)

# Recommendation
