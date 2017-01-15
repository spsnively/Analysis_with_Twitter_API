# Analysis of Trending TV Guide Shows using Twitter API
___
### Author
* Shannon Snively

### Overview
This project analyzes trending tv shows by web scraping their titles and description from [tvguide.com](http://www.tvguide.com/trending-tonight), and querying through the Twitter API. The Twitter API processes tweets containing the titles of the tv shows with the argument of either time (in seconds) or quantity of the tweets the user is interested in collecting.

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
