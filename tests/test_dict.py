def func(dct):
    dct["four"] = 4
    print(dct)


# 字典的值传递传递的是地址
def test_dict():
    dct = {"one": 1, "two": 2, "three": 3}
    print(dct)
    func(dct)
    print(dct)


test_dict()
