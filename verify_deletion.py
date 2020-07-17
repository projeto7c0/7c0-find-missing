import database
import time
import twitter
from datetime import timedelta



def exception_handler(request, exception):
    print(exception)


def verify(ids):
    erased = set()
    if len(ids) > 100:
        id_groups = split(ids, 1+len(ids)//100)
    else:
        id_groups = [ids]

    api = twitter.autentica()
    for id_group in id_groups:
        erased = twitter.check_exists(id_group, api)

        print("atualizando tweets apagados...")
        database.update_erased_tweets(erased)

        print("atualizando todos os tweets checados...")
        database.update_checked(id_group)

        print("Fim de grupo")

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))
