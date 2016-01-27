import encoding_fix
import tweepy
import csv
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
output_file = csv.writer(open("food_data_2.csv", "w"))

class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print(tweet.author.screen_name + "\t" + tweet.text)
        output_file.writerow([tweet.user.screen_name.encode("utf-8"), str(tweet.created_at), tweet.text.encode("utf-8")])

    def on_error(self, status_code):
        print( 'Error: ' + repr(status_code))
        return False

l = StreamListener()
streamer = tweepy.Stream(auth=auth, listener=l)

keywords = ['food', 'hungry']
streamer.filter(track = keywords)
