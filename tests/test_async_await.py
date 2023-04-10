import types
from typing import Coroutine


# def function():
#     return 1
#
#
# def generator():
#     yield 1
#
#
# async def async_function():
#     return 1
#
#
# async def async_generator():
#     yield 1
#
#
# # 下面两种类型比较的方式等价
# # 类型比较的三种方式：is、==、isinstance
# # PEP 8: E721 do not compare types, use 'isinstance()'
# print(type(function) is types.FunctionType)
# print(type(generator()) is types.GeneratorType)
# print(type(async_function()) is types.CoroutineType)
# print(type(async_generator()) is types.AsyncGeneratorType)
#
# # 第一个参数为对象，第二个为类型名或类型名的一个列表
# # 若参数二为一个列表，则若对象类型与元组中类型名之一相同即返回True。
# print(isinstance(function, types.FunctionType))
# print(isinstance(generator(), types.GeneratorType))
# print(isinstance(async_function(), types.CoroutineType))
# print(isinstance(async_generator(), types.AsyncGeneratorType))
#
# print(async_function())


def run(coroutine: Coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value


async def async_function():
    return 1


async def await_coroutine():
    result = await async_function()
    print(result)


run(await_coroutine())
# 1
