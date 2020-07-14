import re, time
import database_auth


def lock_tweets():
    sql = "update mimic_tweets set check_erased = 1 where erased = 0;"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
    except Exception as E:
        print(E)
    finally:
        db.commit()
        db.close()


def get_ids():
    sql = "select idTweets from mimic_tweets where check_erased = 1;"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        value = cursor.fetchall()
    except Exception as E:
        print(E)
    finally:
        db.close()

    return value

def update_erased_tweets(id_set):
    db = database_auth.conecta_banco()
    cursor = db.cursor()

    for id in id_set:
        sql = "update mimic_tweets set timestamp_erased = NOW(), erased = 1, check_erased = 2 where idTweets = \"" + id + "\";"
        try:
            cursor.execute(sql)
        except Exception as E:
            print(E)

    db.commit()
    db.close()

def update_checked(id_set):
    db = database_auth.conecta_banco()
    cursor = db.cursor()

    sql = "update mimic_tweets set check_erased = 2 where idTweets in ("

    for id in id_set:
        sql += "\"" + str(id[0]) + "\","

    sql += "\"0\");"

    # print(sql)
    try:
        cursor.execute(sql)
    except Exception as E:
        print(E)

    db.commit()
    db.close()
