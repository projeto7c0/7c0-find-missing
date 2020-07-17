if __name__ == '__main__':
    import time
    import database
    import verify_deletion
    from random import shuffle

    
    print("iniciando a coleta de ids... ")
    ids = database.get_ids()

    print("Coletados " + str(len(ids)) + " ids para checagem...")

    print("Checando se tweets foram removidos...")
    start_time = time.time()
    verify_deletion.verify(ids)
    end_time = time.time()
    print("Terminado em... ")
    print(end_time - start_time)

