import os
import twitter
import json


class Tweet:
    def __init__(self, app):
        # https://python-twitter.readthedocs.io/en/latest/
        self.api = twitter.Api(consumer_key=os.getenv('TWITTER_CONSUMER_KEY'),
                               consumer_secret=os.getenv('TWITTER_CONSUMER_SECRET'),
                               access_token_key=os.getenv('TWITTER_ACCESS_TOKEN_KEY'),
                               access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
        self.api.sleep_on_rate_limit = False

    def get_list_of_tweets(self, keyword, since, until, num_tweets):
        q = f'q={keyword}&since={since}&until={until}&count={num_tweets}'
        list = self.api.GetSearch(
            raw_query=q)
        print(f'query:  {q}')
        num_objects = len(list)
        print(f'num objects returned: {num_objects}')
        return list

    def get_nodes(self, list_of_tweets):
        list = []
        for t in list_of_tweets:
            list.append(t.user.id)
        return list

    def get_edges(self, list_of_tweets):
        list = []
        for t in list_of_tweets:
            if hasattr(t.retweeted_status, 'user'):
                list.append((t.user.id, t.retweeted_status.user.id))
            if hasattr(t.user_mentions, 'id'):
                list.append((t.user.id, t.user_mentions.id))
        return list
