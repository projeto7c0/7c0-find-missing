if __name__ == '__main__':
    import time
    import database
    import verify_deletion
    from random import shuffle

    start_time = time.time()    
    print("iniciando a coleta de ids... ")

    for i in range(7):
        print("Tentativa " + str(i))
        ids = database.get_ids_election()

        print("Coletados " + str(len(ids)) + " ids para checagem...")

        print("Checando se tweets foram removidos...")

        try:
            verify_deletion.verify_election(ids)
        except Exception as E:
            print(E)
            time.sleep(600)

    end_time = time.time()
    print("Terminado em... ")
    print(end_time - start_time)

