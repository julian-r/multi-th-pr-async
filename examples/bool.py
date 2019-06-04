from timeit import timeit
import threading
import multiprocessing

def local():
    lock = True
    for _ in range(100):
        lock = False
        lock = True

def thread():
    lock = threading.Lock()
    for _ in range(100):
        lock.acquire()
        lock.release()

def mp():
    lock = multiprocessing.Lock()
    for _ in range(100):
        lock.acquire()
        lock.release()

if __name__ == '__main__':
    print('local', timeit(local, number=1000000))
    print('threading', timeit(thread, number=1000000))
    print('mp', timeit(mp, number=1000000))
