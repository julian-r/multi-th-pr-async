# "compute" intense task

from timeit import timeit
from threading import Thread
from multiprocessing import Process
import asyncio

COUNT = 500000000


def test(count):
    print("test called")
    for i in range(count):
        1 + 1


def pure():
    test(COUNT)


def with_threading():
    t1 = Thread(target=test, args=(COUNT // 2,))
    t2 = Thread(target=test, args=(COUNT // 2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def with_mp():
    p1 = Process(target=test, args=(COUNT // 2,))
    p2 = Process(target=test, args=(COUNT // 2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


async def test_wrapper(count):
    return test(count)


async def async_main():
    asyncio.gather(test_wrapper(COUNT // 2), test_wrapper(COUNT // 2))


def with_asyncio():
    asyncio.run(async_main())


if __name__ == "__main__":
    print('threading')
    print(timeit(with_threading, number=1))
    print('mp')
    print(timeit(with_mp, number=1))
    print('pure')
    print(timeit(pure, number=1))
    print('aio')
    print(timeit(with_asyncio, number=1))

