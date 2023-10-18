import tweepy
import requests
from bs4 import BeautifulSoup

# Twitter API credentials
consumer_key = "1Q2mOsv7mhO1HFFJK4hHO34K0"
consumer_secret = "vI66HKqTSSjbbcpg79sSq53kakR1cUDNGG93AodQyfg6s0pKRF"
access_token = "1605883142690471936-izBzCiSXycqKjbHoo6m97sCuaD7iKH"
access_token_secret = "access token secret j0aqm4psLMl9VBHcw2QojwRyKsQHaMVHhk2u75kECyRly"

# Hashnode blog RSS feed URL
hashnode_rss_url = "https://saiprajoth.hashnode.dev/rss.xml"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to check for new blog posts
def check_for_new_posts():
    # Fetch the RSS feed
    response = requests.get(hashnode_rss_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'xml')
        items = soup.find_all('item')
        # Assuming the first item is the latest post
        latest_post = items[0]
        post_title = latest_post.title.text
        post_url = latest_post.link.text
        # Check if this post has already been tweeted
        # You can use a database or file to store and track tweeted posts
        if post_not_already_tweeted(post_url):
            # Tweet the new blog post
            tweet_text = f"New blog post: {post_title} {post_url}"
            api.update_status(tweet_text)
            mark_post_as_tweeted(post_url)

# Function to check if a post has already been tweeted
def post_not_already_tweeted(post_url):
    # Implement your logic here to check if the post URL is already in your database or file
    # Return True if it hasn't been tweeted, False otherwise

# Function to mark a post as tweeted
def mark_post_as_tweeted(post_url):
    # Implement your logic here to record the tweeted post URL in your database or file

# Run the check_for_new_posts function
check_for_new_posts()

