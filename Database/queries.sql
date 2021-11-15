--check tables
SELECT * FROM initial_tweets_table;
SELECT * FROM api_tweets_table;
SELECT * FROM api_count_table;

--compare total number of tweets vs collected tweets
WITH t1 AS (
	SELECT created_date, COUNT (score) AS collected_count
	FROM api_tweets_table
	GROUP BY created_date)
SELECT act.created_date, act.weekday, act.tweet_count AS total_count, t1.collected_count,
	ROUND(t1.collected_count*1.0 / act.tweet_count * 100, 2) AS percentage_collected
FROM api_count_table AS act
JOIN t1
	ON act.created_date = t1.created_date

--compare number of collected positive and negative tweets
SELECT created_date, weekday,
	COUNT (score) AS collected_count,
	SUM(CASE WHEN score = 0 THEN 1 ELSE 0 END) AS negative_count,
	SUM(CASE WHEN score = 1 THEN 1 ELSE 0 END) AS positive_count
FROM api_tweets_table
GROUP BY created_date, weekday
ORDER BY created_date ASC

--compare percentage of positive and negative tweets by weekday
WITH t1 AS(
	SELECT weekday,
		COUNT (score) AS collected_count,
		SUM(CASE WHEN score = 0 THEN 1 ELSE 0 END) AS negative_count,
		SUM(CASE WHEN score = 1 THEN 1 ELSE 0 END) AS positive_count
	FROM api_tweets_table
	GROUP BY weekday)
SELECT t1.weekday, 
        ROUND(t1.positive_count*1.0 / t1.collected_count * 100, 2) AS positive_percentage,
		ROUND(t1.negative_count*1.0 / t1.collected_count * 100, 2) AS negative_percentage
FROM t1
ORDER BY 
    CASE
        WHEN weekday = 'Sunday' THEN 1
        WHEN weekday = 'Monday' THEN 2
        WHEN weekday = 'Tuesday' THEN 3
        WHEN weekday = 'Wednesday' THEN 4
        WHEN weekday = 'Thursday' THEN 5
        WHEN weekday = 'Friday' THEN 6
        WHEN weekday = 'Saturday' THEN 7
    END ASC