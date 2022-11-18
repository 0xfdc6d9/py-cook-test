from enum import Enum


class Status(Enum):
    A = 1
    B = 2


# 枚举类要想获得数值的话后面还要点value
def test_enum():
    print(type(Status.A), Status.A)
    print(type(Status.A.value), Status.A.value)


test_enum()
