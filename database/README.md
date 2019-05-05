# Anime-Recommendation-Pipeline

# Database and Deployment 
+ mysql 8.0 on Google Cloud

# tables
+ **anime**: anime data from kaggle dataset, contains all animes' features
+ **rating**: rating data from kaggle dataset, contains all user's ratings
+ **favorite**: top rated animes for all users, used fro cf recommendation 
+ **item**: item's id and name, used for speeding up query
+ **user**: user's account and password, used for verification
+ **user_sim**: cf based recommendation result
+ **content_based**: content based recommendation result

# Optimization
We split the table to speed up query, in our project, the table **item** is used for speed up content-based recommendation

# Data Access Layer
For more efficiency of other services to communicate with database, we also build a logical API called database.py, which includes several functions that save the more frequent operations with database. 

