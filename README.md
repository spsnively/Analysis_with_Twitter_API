# Analysis of Trending TV Guide Shows using Twitter API
___
### Author
* Shannon Snively
* Colin Cambo

### Overview
This project allows users to analyze what the latest and greatest trending tv shows are through twitter feeds. The way the code is designed to work is by web scraping [tvguide.com](http://www.tvguide.com/trending-tonight) for trending tv show titles and descriptions. The titles are stored in a list that is then queried through the Twitter API based on either the amount of tweets containing show titles or a given time (in seconds) that the twitter API will receive tweets from. 

### Requirements
Before running this code you will need to create a new file within the directory called config_secret.json and insert your Twitter API keys in the following format:

```python 
{
    CONSUMER_KEY:"CONSUMER_KEY",
    CONSUMER_SECRET:"CONSUMER_SECRET",
    OAUTH_TOKEN:"OAUTH_TOKEN",
    OAUTH_TOKEN_SECRET:"OAUTH_TOKEN_SECRET"
}
```
