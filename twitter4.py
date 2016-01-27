import encoding_fix
import tweepy
import csv
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# code to write the file
output_file = csv.writer(open("food_data.csv", "w"))

public_tweets = api.search("food", count=50)

for tweet in public_tweets:
    print(tweet.user.screen_name + "\t" + str(tweet.created_at) + "\t" + tweet.text)
    output_file.writerow([tweet.user.screen_name.encode("utf-8"), str(tweet.created_at), tweet.text.encode("utf-8")])

