import sys
import time
from functools import wraps
from threading import Thread

N = 100000


def count_down(n):
    while n > 0:
        n -= 1
    return


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.process_time()
        result = func(*args, **kwargs)
        elapsed_time = time.process_time()
        print("Time used:", (elapsed_time - start_time))
        return result

    return wrapper


@timer
def func1():
    count_down(N)


@timer
def func2():
    t1 = Thread(target=count_down, args=[N // 2])
    t2 = Thread(target=count_down, args=[N // 2])
    t1.start()
    t2.start()
    t1.join()
    for i in range(100):
        t2.join()


if __name__ == '__main__':
    # func1()
    func2()
    print(sys.getrefcount(N))