import tweepy
import twitter_auth


def check_exists(id_group, api):
    tweets = []
    ids = []
    for id in id_group:
        #print(id[0])
        ids.append(str(id[0]))

    #print(ids)
    if len(ids) > 0:
        for status in api.statuses_lookup(ids):
            #print(status.id_str)
            tweets.append(status.id_str)
        
    print("ids apagados: " + str(len(ids) - len(tweets)))
    # print("ids retornados: " + str(len(tweets)))

    erased = set(ids) - set(tweets)

    return erased

def autentica():
    api = twitter_auth.autentica_search()
    return api