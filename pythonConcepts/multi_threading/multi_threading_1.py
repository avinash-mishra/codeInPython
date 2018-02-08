import threading


def worker():
    """
    thread worker function
    :return:
    """
    print("worker")


threds = []
for i in range(5):
    t = threading.Thread(target=worker)
    threds.append(t)
    t.start()


