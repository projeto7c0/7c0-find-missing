if __name__ == '__main__':
    import database

    database.lock_tweets()
    database.lock_tweets_election()