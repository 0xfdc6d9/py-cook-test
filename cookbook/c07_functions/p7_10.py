def a():
    def apply_async(func, args, callback):
        result = func(*args)
        callback(result)

    def add(x, y):
        return x + y

    def print_result(result):
        print(result)

    apply_async(add, (2, 3), callback=print_result)
    apply_async(add, (4, 5), callback=print_result)


def b():
    def appy_async(func, args, *, callback):
        result = func(*args)
        callback(result)

    def add(x, y):
        return x + y

    class ResultHandler(object):
        def __init__(self):
            self.sequence = 0

        def handle(self, result):
            self.sequence += 1
            print("[{}] Got: {}".format(self.sequence, result))

    r = ResultHandler()
    appy_async(add, (2, 3), callback=r.handle)
    appy_async(add, (4, 5), callback=r.handle)


a()
print("<========================>")
b()
