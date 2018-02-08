
import threading

def worker(arg1, arg2):
    """
    thread worker function
    :return:
    """
    print("arg1 is %s arg2 is %s" % (arg1, arg2))


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=("hi", "bye"))
    threads.append(t)
    t.start()

