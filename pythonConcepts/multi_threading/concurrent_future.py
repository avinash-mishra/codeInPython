from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from time import sleep

"""
Demo for process pooling and thread pooling
"""


def return_after_5_secs(msg):
    sleep(5)
    return msg

"""
Use thread pooling when the task requires too much network operations and I/O
"""
def run_thread_pool():
    print("running thread pool")
    pool = ThreadPoolExecutor(3)
    future = pool.submit(return_after_5_secs, ("hello"))
    print(future.done())
    # sleep(5)
    print(future.done())
    print(future.result())

"""
Use process pooling is good for CPU intensive tasks
"""
def run_process_pool():
    print("running process pool")
    pool = ProcessPoolExecutor(3)
    future = pool.submit(return_after_5_secs, ("hello"))
    print(future.done())
    print(future.done())
    print(future.result())

run_thread_pool()
run_process_pool()