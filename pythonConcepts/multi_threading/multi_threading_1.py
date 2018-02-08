import threading


def worker():
    """
    thread worker function
    :return:
    """
    print(threading.get_ident())
    print("worker")


threds = []
for i in range(5):
    t = threading.Thread(target=worker)
    threds.append(t)
    t.start()


