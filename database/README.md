# Anime-Recommendation-Pipeline

# Database
+ mysql 8

# tables
+ **anime**: anime data from kaggle dataset, contains all animes' features
+ **rating**: rating data from kaggle dataset, contains all user's ratings
+ **favorite**: top rated animes for all users, used fro cf recommendation 
+ **item**: item's id and name, used for speeding up query
+ **user**: user's account and password, used for verification
+ **user_sim**: cf based recommendation result
+ **content_based**: content based recommendation result

