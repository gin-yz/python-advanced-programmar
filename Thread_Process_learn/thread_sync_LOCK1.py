from threading import Lock, Thread

total = 0
lock = Lock()

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
        total -= 1
        lock.release()


if __name__ == '__main__':

    thread1 = Thread(target=add)
    thread2 = Thread(target=desc)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(total)
