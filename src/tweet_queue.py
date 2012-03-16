import twitter

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

class TweetQueue:
    def __init__(self, api):
        self.api = api
        self.queue = []
    
        try:
            self.last_tweet = api.GetMentions()[0]
        except IndexError:
            self.last_tweet = None

    def _fetch_tweets(self):
        if self.last_tweet:
            self.queue = self.api.GetMentions(since_id=self.last_tweet.id)
        else:
            self.queue = self.api.GetMentions()

        if self.queue:
            self.last_tweet = self.queue[0]

    def peek(self):
        if not self.queue:
            self._fetch_tweets()
        if self.queue:
            return self.queue[-1]

    def poll(self):
        if not self.queue:
            self._fetch_tweets()

        if self.queue:
            return self.queue.pop(-1)
    
tq = None

def get():
    global tq
    if not tq:
        api = twitter.Api()
        api.SetCredentials(
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret)
        tq = TweetQueue(api)
    
    return tq
