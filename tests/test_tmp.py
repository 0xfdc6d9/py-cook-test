import threading

n = 0


def foo():
    global n
    n += 1


def func1():
    threads = []
    for i in range(10000):
        t = threading.Thread(target=foo)
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(n)


if __name__ == '__main__':
    for _ in range(100):
        func1()
