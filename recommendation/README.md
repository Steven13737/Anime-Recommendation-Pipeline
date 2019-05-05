# Anime-Recommendation-Pipeline
Project for Data Pipeline

## Offline training service: 

  + Content-based recommendation: 

    + In this part, given that it’s more efficient to return the results from the back end to the front end by saving the similarity matrix into the database first and querying them, we plan to train it locally and save the file into the **MySQL database**. When the new anime comes in, we can update the anime.csv and train them again to produce a new csv to save into the database. Repeat this method periodically. 

    + For this part, we did feature engineering and build a **KNN** model to calculate the similarities between different anime. 

 

  + Collaborative Filter recommendation: 

    + We trained a CF model locally to predict potential anime that users may like. For every user, we’ll recommend the anime based on users similar with him and their preference. We first calculate the similarity matric among users. Then, we calculate the top 5 movies with the highest score for each user.  We save them into the database and update weights from database as well. 

 

## Online predict service: 

+ This service will be always listening to the queue reader **(kafka)** once service is starting. If there’re parameters (user_id) about what the predict service needs to recommend passing into the kafka, predict service will return the recommendation results back to the queue reader. The front end is always listening to the queue as well in order to receive the results of the recommendation.  
