# Twitter-Sentiment-Analysis

## Project Overview
The purpose of this project was to create a Twitter sentiment monitoring dashboard. By applying NLP, a dataset of over 50K pre-labeled tweets classified into positive, negative, and neutral was used to train and test different machine learning models. New tweets were collected via the Twitter API v2 and passed into the selected model to predict sentiment. The dashboard presents analysis of sentiment by weekday. For the purpose of this project, topic selected was Tesla.

### Resources
- Data Source: [SemEval-2017 Twitter data](https://alt.qcri.org/semeval2017/task4/) and Twitter API v2
- Language: 
    - Python
        - Dependecies: numpy, pandas, nltk, matplotlib, re, scikit-learn
    - Pyspark
    - JavaScript, HTML
        - Libraries: Bootstrap, D3, plotly, anychart
- Software: Jupyter Notebook, VSCode, Google Colab, pgAdmin, AWS
- Code/Notebooks:
    - [Data Cleaning](Cleaning_PseudoCode/Final_Data_Cleaning.ipynb)
    - [Machine Learning](Modeling/Practice_Modeling_InitialData.ipynb)
    - [Twitter API data gathering](Twitter%20V2%20API%20Call%20Final%20with%20Looping.ipynb)
    - [Cleaning and Scoring API data](clean_score_tweets.ipynb)
    - [Database ETL](Database/ETL.ipynb)
    - [JavaScript]() - no link yet
    - [HTML]() - no link yet
- **[Link to interactive dashboard]()** - no link yet
- **[Link to slides]()** - no link yet

## Method

### A. Data Gathering
1. Sem-Eval Dataset - The dataset contains tweets categorized to into three labels: positive, negative, and neutral. 
2. New Tweets - collected via Standard Basic Twitter API v2. Endpoints used were search tweets and tweet counts where API limitation is set to query only the most recent 7 days. Data gathered was from Nov1-14 (two weeks). 

### B. Data Cleaning
- A function was created to clean the tweets using regular expression to remove retweets, hyperlinks, hashtags, numbers, emojis, and mentions. NLP was applied by tokenizing the tweets, removing stop words, and lemmatizing the list of words by utilizing the NLTK library.
- A second function was created to apply the cleaning function, build the dataframe, and assign scores (1:positive, 0:neutral, -1:negative) to each tweet accordingly. 

### C. Machine Learning
- Preprocessing of data: Using a .py file, the cleaning function was applied on the new tweets to be able to feed it to the model for sentiment prediction.
- Bernoulli Naive Bayes 
- Linear Support Vector Classification 
- Logistic Regression
- Metrics measured and compared were precision, recall, F1 scores, and confusion matrix.

### D. Database
- An AWS RDS instance was created and connected to pgAdmin where a new database was created. Tables were generated using the schema.
- Data files were uploaded to an S3 bucket where PySpark was used to extract and transform the data to match the tables in pgAdmin.
- Connection was made to the AWS RDS instance to write the dataframes created to the tables in the RDS. 

### E. Interactive App/Dashboard
- Filter by weekday
- Number of tweets by sentiment
- Sample 5 tweets
- Overall sentiment distribution    
- Line chart of sentiment distribution by hour
- Bar chart and word cloud of most common words 

## References

- Edward, A. (2021, June 13). *An Extensive Guide to collecting tweets from Twitter API v2 for academic research using Python 3*. Towards Data Science. https://towardsdatascience.com/an-extensive-guide-to-collecting-tweets-from-twitter-api-v2-for-academic-research-using-python-3-518fcb71df2a

- Goyal, G.(2021, June 11). *Twitter Sentiment Analysis- A NLP Use-Case for Beginners*. Analytics Vidhya. https://www.analyticsvidhya.com/blog/2021/06/twitter-sentiment-analysis-a-nlp-use-case-for-beginners/

- Effrosynidis, D. (2019). *text-preprocessing-techniques*. Github. https://github.com/Deffro/text-preprocessing-techniques

Other useful articles:
- https://developer.twitter.com/en/docs/twitter-api/early-access 




https://user-images.githubusercontent.com/84211948/142151062-d152ca18-510c-4fce-9e55-89386307a85c.mp4


