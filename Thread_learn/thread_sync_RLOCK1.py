# 同一线程里可以多次调用RLOCK，不会引发死锁，不同进程间和LOCK相同

from threading import RLock, Thread

total = 0
lock = RLock()

def add():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        total += 1
        lock.release()


def desc():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        lock.acquire()
        total -= 1
        lock.release()
        lock.release()


if __name__ == '__main__':

    thread1 = Thread(target=add)
    thread2 = Thread(target=desc)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(total)
