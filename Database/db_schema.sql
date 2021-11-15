-- This table will contain pre-labeled tweets for cleaning to be used in the model
CREATE TABLE initial_tweets_table (
  attitude TEXT NOT NULL,
  tweets TEXT
);

-- This table will contain API data and its predicted score
CREATE TABLE api_tweets_table (
  created_at VARCHAR NOT NULL, 
  created_date DATE NOT NULL,
  weekday TEXT NOT NULL,
  hours INTEGER NOT NULL,  
  tweet TEXT NOT NULL,
  text TEXT NOT NULL, 
  score INTEGER NOT NULL
);

-- This table will contain API data count per day
CREATE TABLE api_count_table (
  end_time VARCHAR NOT NULL,
  start_time VARCHAR NOT NULL,
  created_date DATE PRIMARY KEY NOT NULL,
  weekday TEXT NOT NULL,
  tweet_count INTEGER NOT NULL
);