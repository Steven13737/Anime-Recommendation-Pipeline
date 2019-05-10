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
[details Recommendation](https://github.com/Steven13737/Anime-Recommendation-Pipeline/blob/master/recommendation)



# Demo
**After running the system, we can login to our recommendation system**
![Login Page](https://github.com/Steven13737/Anime-Recommendation-Pipeline/blob/master/src/Login.png)

**Then, the back-end will verify the user's identity and retrive the cf recommendation content from database. Then in the web page, we use Ajax to help user get content-based recommendation content. we show the user's information and recommendation items here**
![CF based Recommendation](https://github.com/Steven13737/Anime-Recommendation-Pipeline/blob/master/src/Recommendation.png)
![Content based Recommendation](https://github.com/Steven13737/Anime-Recommendation-Pipeline/blob/master/src/Recommendation2.png)

**To monitor our system status, we can fetch the running information from back end**
![Back-end log](https://github.com/Steven13737/Anime-Recommendation-Pipeline/blob/master/src/log.png)
