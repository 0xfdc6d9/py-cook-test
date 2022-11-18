def mygen():
    yield 1

    yield 2

    # yield 返回3，然后将send过来的msg保存到recv
    recv = yield 3

    yield f"{recv} 这是mygen收到的msg"


a = mygen()

# ret = next(a)  # 等同于 a.send(None)
ret = a.send(None)
print(ret)

ret = a.send('hello 1')
print(ret)

ret = a.send('hello 2')
print(ret)

ret = a.send('hello 3')
print(ret)
