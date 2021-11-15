#import dependencies
import pandas as pd
from datetime import datetime
import json

#load API data
api_tweets_df = pd.read_csv("API_data.csv")
#drop id column
api_tweets_df = api_tweets_df.drop(columns="id")

# Convert date column from object to datetime format
api_tweets_df['created_date'] = pd.to_datetime(api_tweets_df['created_at'], format='%Y-%m-%d %H:%M:%S')
# Add a weekday column
api_tweets_df['weekday'] = api_tweets_df['created_date'].dt.day_name()
# Add an hour column
api_tweets_df['hours'] = api_tweets_df['created_date'].dt.strftime('%H')
# Convert date format
api_tweets_df['created_date'] = api_tweets_df['created_date'].dt.strftime('%Y-%m-%d')

# Change column names and reorder columns
api_tweets_df = api_tweets_df[['created_at','created_date','weekday','hours','tweet']]
# Convert tweets to list for cleaning
api_tweet_list = api_tweets_df["tweet"].tolist()

# import cleaning function
from Cleaning_PseudoCode.Final_Data_Cleaning import clean_tweets_func
# create function to make text df
def create_text_df():
    text = clean_tweets_func(api_tweet_list)
    text_df = pd.DataFrame({"text":text})
    return text_df

# call create_text_df function
text_df = create_text_df()
# make list to list of strings so model can be applied
text_df["text_string"] = text_df["text"].apply(lambda x: str(x))

# split data in 3 to be able to run the model
text_df1 = text_df.iloc[:20000]
text_df2 = text_df.iloc[20000:40000]
text_df3 = text_df.iloc[40000:60000]
text_df4 = text_df.iloc[60000:]

# import vertorizer and model
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# load vectorizer and machine learning model
vectorizer = pickle.load(open('Modeling/vectorizer.pkl', 'rb'))
model = pickle.load(open('Modeling/model.pkl', 'rb'))

# vectorize and predict first 1/4 of data
tweet_predict1 = text_df1["text_string"]
tweet_vectorized1 = vectorizer.transform(tweet_predict1).toarray()
prediction1 = model.predict(tweet_vectorized1)

# vectorize and predict second 1/4 of data
tweet_predict2 = text_df2["text_string"]
tweet_vectorized2 = vectorizer.transform(tweet_predict2).toarray()
prediction2 = model.predict(tweet_vectorized2)

# vectorize and predict third 1/4 of data
tweet_predict3 = text_df3["text_string"]
tweet_vectorized3 = vectorizer.transform(tweet_predict3).toarray()
prediction3 = model.predict(tweet_vectorized3)

# vectorize and predict last 1/4 of data
tweet_predict4 = text_df4["text_string"]
tweet_vectorized4 = vectorizer.transform(tweet_predict4).toarray()
prediction4 = model.predict(tweet_vectorized4)

# create df of scored tweets
prediction_df1 = pd.DataFrame(prediction1, columns=["score"])
prediction_df2 = pd.DataFrame(prediction2, columns=["score"])
prediction_df3 = pd.DataFrame(prediction3, columns=["score"])
prediction_df4 = pd.DataFrame(prediction4, columns=["score"])
# combine 
prediction_df = pd.concat([prediction_df1, prediction_df2, prediction_df3, prediction_df4])

# combine dataframes
combined_prediction_df = pd.concat([api_tweets_df, text_df["text"], prediction_df],axis=1)
combined_prediction_df.head()

# save scored tweets
combined_prediction_df.to_csv('cleaned_scored_tweets.csv', index = False)
# save to json format 
combined_prediction_df.to_json('cleaned_scored_tweets.json', orient='records')

# load counts data
counts_df = pd.read_csv("API_count_data.csv")
# Convert date column from object to datetime format
counts_df['created_date'] = pd.to_datetime(counts_df['start'], format='%Y-%m-%d %H:%M:%S')
# Add a weekday column
counts_df['weekday'] = counts_df['created_date'].dt.day_name()
# Convert date format
counts_df['created_date'] = counts_df['created_date'].dt.strftime('%Y-%m-%d')

# Change column names and reorder columns
counts_df = counts_df[['end_time','start_time','created_date','weekday','tweet_count']]
# save to csv format
counts_df.to_csv('tweets_count.csv', index = False)
# save to json format
counts_df.to_json('tweets_count.json', orient='records')
