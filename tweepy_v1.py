import tweepy
import pandas as pd

# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''


# Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api
    


# Create API object
api = connect_to_twitter_OAuth()


""" public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text) """

""" user = api.get_user('realdonaldtrump')
print(user.screen_name)
print(user.followers_count)
print(user.location) """

query = input('Enter your tweet query:') #no retweets = -RT
n_item = int(input('Enter no. of tweets to get:'))
data_csv = input('Enter csv name:')
    
tweet_id = []
tweet_text = []
tweet_createdat = []
tweet_location = []
tweet_list = []
for tweet in tweepy.Cursor(api.search, q='-RT'+query, lang='en', geocode = '',).items(n_item): 
    t_id = tweet.id
    t_text = tweet.text
    t_createdat = tweet.created_at
    t_location = tweet.user.location
    """ tweet_id.append(t_id)
    tweet_text.append(t_text)-
    tweet_createdat.append(t_createdat)
    tweet_location.append(t_location) """
    tweet_list.append({'tweet_id':t_id,
                        'text':t_text, 
                        'createdat':t_createdat, 
                        'location':t_location})

#df = pd.DataFrame({'id':tweet_id,'text':tweet_text,'datecreated':tweet_createdat, 'location':tweet_location})
df = pd.DataFrame(tweet_list, columns=['tweet_id','text','createdat','location'])
df.to_csv(data_csv, index = False)
#print(df)
print('Done')