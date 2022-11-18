# hashlib 好像只能这么使用
import hashlib
import time


def test_hashlib():
    value = str(time.time())
    m = hashlib.md5()
    m.update(value.encode("UTF-8"))
    return m.hexdigest()


print(test_hashlib())
