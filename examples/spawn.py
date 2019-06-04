from timeit import timeit
import threading
import multiprocessing

def target():
    pass

def local():
    for _ in range(100):
        target()

def thread():
    for _ in range(100):
        threading.Thread(target=target).start()

def mp():
    for _ in range(100):
        multiprocessing.Process(target=target).start()


if __name__ == '__main__':
    number = 1000
    print('local', timeit(local, number=number))
    timeit('threading.Thread(target=target).start()', number=number, globals=globals())
    timeit('multiprocessing.Process(target=target).start()', number=number, globals=globals())

