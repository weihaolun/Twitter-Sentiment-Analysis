import nltk          
nltk.download('stopwords')
import re                                  
import string                             
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer 
import pandas as pd
import numpy as np

# Function to clean tweets
def clean_tweets_func(tweets_lem): 

    #Remove Retweets
    def remove_RT(tweets_lem):
        return re.sub(r'^RT[\s]+', '', str(tweet))

    removed_RT = []
    for tweet in tweets_lem:
        x = remove_RT(tweet)
        removed_RT.append(x)

    #Remove Hyperlinks
    def remove_HL(removed_RT):
        return re.sub(r'https?:\/\/.*[\r\n]*', '', str(tweet))

    removed_HL = []
    for tweet in removed_RT:
        x = remove_HL(tweet)
        removed_HL.append(x)

    #Remove Hashtags
    def remove_Hash(removed_HL):
        return re.sub(r'#', '', str(tweet))
    
    removed_Hash = []
    for tweet in removed_HL:
        x = remove_Hash(tweet)
        removed_Hash.append(x)

    #Remove Numbers 
    def remove_Numbers(removed_Hash):
        return re.sub(r'[0-9]', '', str(tweet))

    removed_Numbers = []
    for tweet in removed_Hash:
        x = remove_Numbers(tweet)
        removed_Numbers.append(x)

    #Remove Emojis 
    def remove_Emojis(removed_Numbers):
        emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U00002500-\U00002BEF"  # chinese char
            u"\U00002702-\U000027B0"
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            u"\U0001f926-\U0001f937"
            u"\U00010000-\U0010ffff"
            u"\u2640-\u2642"
            u"\u2600-\u2B55"
            u"\u200d"
            u"\u23cf"
            u"\u23e9"
            u"\u231a"
            u"\ufe0f"                  # dingbats
            u"\u3030"
                               "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', str(tweet))

    removed_Emojis = []
    for tweet in removed_Numbers:
        x = remove_Emojis(tweet)
        removed_Emojis.append(x)

    #Remove Mentions 
    def remove_Mentions(removed_Emojis):
        return re.sub("@[A-Za-z0-9_]+","", str(tweet))

    removed_Mentions = []
    for tweet in removed_Emojis:
        x = remove_Mentions(tweet)
        removed_Mentions.append(x)

    #Remove other non alphanumeric characters
    removed_Nonalnum = []
    for tweet in removed_Mentions:
        x = tweet.replace("“", "")
        x = tweet.replace("·", "")
        x = tweet.replace("’", "")
        removed_Nonalnum.append(x)
    
    #Store finished product from above extractions in tweet2
    tweet2 = removed_Nonalnum

    #Tokenizer
    def Tokenizer(tweet2):
        # instantiate the tokenizer class
        tokenizer = TweetTokenizer(preserve_case=False, 
                               strip_handles=True,
                               reduce_len=True)
        return tokenizer.tokenize(tweet)

    Tokenized = []
    for tweet in tweet2:
        x = Tokenizer(tweet)
        Tokenized.append(x)

    #Import the english stop words list from NLTK
    stopwords_english = stopwords.words('english') 

    #Removing stop-words and punctuation (we may want to customize the stop-word list and/or the punctuation )
    tweets_clean = []
    for i in range(len(Tokenized)):
        row = []
        for element in Tokenized[i]: #Go through every individual word
            if (element not in stopwords_english and  # remove stopwords
            element not in string.punctuation): # remove punctuation
                row.append(element)
        tweets_clean.append(row)
        i+=1

    #Lemmatization
    # Instantiate lemming class
    lemmatizer = WordNetLemmatizer()
    # Create an empty list to store the stems
    tweets_lem = []
    for i in range(len(tweets_clean)):
        row =[]
        for word in tweets_clean[i]:
            lem_word = lemmatizer.lemmatize(word)  # stemming word
            row.append(lem_word)  # append to the list
        tweets_lem.append(row)
        i+=1

    return(tweets_lem)