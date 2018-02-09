from concurrent.futures import ThreadPoolExecutor
import time


def with_thread_pool():
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(pow, 323, 1235)
        print(future.result())
    print("----- %s seconds----" %(time.time() - start_time))

def without_thread_pool():
    start_time = time.time()
    print(pow(323, 1235))
    print("----- %s seconds----" %(time.time() - start_time))



without_thread_pool()
# with_thread_pool()