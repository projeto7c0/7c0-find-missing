import tweepy
import twitter_auth


def check_exists(id_group):
    api = twitter_auth.autentica_search()

    tweets = []
    ids = []
    for id in id_group:
        #print(id[0])
        ids.append(str(id[0]))

    #print(ids)
    for status in api.statuses_lookup(ids):
        #print(status.id_str)
        tweets.append(status.id_str)
        
    print("ids testados: " + str(len(ids)))
    print("ids retornados: " + str(len(tweets)))

    erased = set(ids) - set(tweets)

    return erased
