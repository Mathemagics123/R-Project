import snscrape
import os
import pandas as pd

class Twitter:

    @staticmethod
    def base_query(query, endpoint, start_date=None, end_date=None, limit=100):
        os.system("snscrape --format '{id}, {date}, {username}, \"{content!r}\", {url}'" # {likeCount}, {retweetCount}, {replyCount}, {quoteCount}, 
                + f" --max-results {limit}"
                + (f"--since {start_date}" if start_date else "")
                + f" {endpoint} '{query}"
                + (f" until:{end_date}" if end_date else "")
                + "' > stdout.txt")

        column_names = ['id', 'date', 'username', 'content', 'url']
        df = pd.DataFrame(columns=column_names)
        if os.stat("stdout.txt").st_size == 0:
            counter = 0
        else:
            df = pd.read_csv('stdout.txt', names=column_names)
            counter = df.count

        os.remove("stdout.txt")
        print(f"Found {counter} results for {query}")
        
        return df

    @staticmethod
    def query_search(search, start_date=None, end_date=None, limit=100):
        return Twitter.base_query(search, "twitter-search", start_date, end_date, limit)

    @staticmethod
    def query_hashtag(hashtag, start_date=None, end_date=None, limit=100):
        return Twitter.base_query(hashtag, "twitter-hashtag", start_date, end_date, limit)

    @staticmethod
    def query_user(user, start_date=None, end_date=None, limit=100):
        return Twitter.base_query(user, "twitter-user", start_date, end_date, limit)

    @staticmethod
    def query_thread(tweet_id, start_date=None, end_date=None, limit=100):
        return Twitter.base_query(tweet_id, "twitter-thread", start_date, end_date, limit)

    @staticmethod
    def query_list_posts(list, start_date=None, end_date=None, limit=100):
        return Twitter.base_query(list, "twitter-list-posts", start_date, end_date, limit)
    
    @staticmethod
    def query_list_members(list, start_date=None, end_date=None, limit=100):
        return Twitter.base_query(list, "twitter-list-members", start_date, end_date, limit)
