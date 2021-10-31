# Twitter-Sentiment-Analysis

## Project Overview
The purpose of this project is to create a real-time Twitter Sentiment Monitoring Web App. By applying NLP, a dataset of over 50K pre-labeled tweets classified into positive, negative, and neutral will be used to train and test the machine learning model. New tweets will be collected via the Twitter API and these will be passed into the model to predict sentiment. Analysis results will show in the Web App alongside other visualizations (tbd).

### Resources
- Data Source: [SemEval-2017 Twitter data](https://alt.qcri.org/semeval2017/task4/) and Twitter API
- Language: Python
    - Dependecies: numpy, pandas, nltk, matplotlib, re, scikit-learn, tweepy
- Software: Jupyter Notebook
- Notebooks:
    - [Practice_Cleaning_Function](Cleaning_PseudoCode/Practice_Cleaning_Function.ipynb)
    - [practice_twitter_api](practice_twitter_api.ipynb)
    - [practice_modeling](Modeling/Practice_Modeling_InitialData.ipynb)

## Method

### A. Data Gathering
1. Sem-Eval Dataset - The dataset contains tweets categorized to into three labels: positive, negative, and neutral. 
2. New Tweets - collected via Twitter Standard Search API using Tweepy library. JSONParser will be used to read tweets in JSON format in preparation for dataframe creation and cleaning.

### B. Data Cleaning
- A function was created to clean the tweets. This uses regular expression to remove retweets, hyperlinks, hashtags, numbers, emojis, and mentions. NLP was applied by tokenizing the tweets, removing stop words, and then stemming the list of words by utilizing the NLTK library.
- A second function was created to apply the cleaning function, build the dataframe, and assign scores (1:positive, 0:neutral, -1:negative) to each tweet accordingly. 
- The cleaning function will be applied on the new tweets to match the format of the data to be preprocessed for sentiment prediction.

### C. Machine Learning
- Preprocessing of data
- Multiple supervised ML algorithms will be tested on the Sem-Eval dataset (possible algorithms to try: Bernoulli Naive Bayes, SVM Multiclass, Multinomial Linear Regression, Decision Trees, Random Forest, k-Nearest Neighbors, and Gradient Boosting).
- Metrics to measure and compare will be accuracy, F1 scores, and confusion matrix. The highest performing model will be used to predict sentiment of new tweets collected.

### D. Database
- Looking into MongoDB to store cleaned data used for the model as well as the new tweets

### E. Interactive App/Dashboard
TBD:
- Plot that shows the sentiments: uses matplotlib’s animation capabilities to refresh the plot. If the tweet is positive, the y-axis gets +1, if negative -1 and for neutral +0.
- dynamic heatmap for the United States showing sentiment (3 colors) by state 
- Word cloud or bar chart of most common words by sentiment
- Gauge of overall sentiment

## References
