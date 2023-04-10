import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main0():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


#

async def main1():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

# https://docs.python.org/zh-cn/3/library/asyncio-task.html#coroutines
# 3.11 asyncio.TaskGroup
# async def main2():
#     async with asyncio.TaskGroup() as tg:
#         task1 = tg.create_task(
#             say_after(1, 'hello'))
#
#         task2 = tg.create_task(
#             say_after(2, 'world'))
#
#         print(f"started at {time.strftime('%X')}")
#
#     # The wait is implicit when the context manager exits.
#
#     print(f"finished at {time.strftime('%X')}")


asyncio.run(main1())
