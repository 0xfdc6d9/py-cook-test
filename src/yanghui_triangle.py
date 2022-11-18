def triangles():
    lst = [1]
    while True:
        yield lst
        lst = [1] + [lst[i] + lst[i + 1] for i in range(len(lst) - 1)] + [1]


t = triangles()
print(type(t))
while True:
    next(t)
