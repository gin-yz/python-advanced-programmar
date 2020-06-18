from queue import Queue
from threading import Thread
import os


def thread_put(name,queue):
    print('start put %s:%s' % (name, os.getpid()))
    for i in range(1000):
        queue.put(i)
    print('end put %s:%s' % (name, os.getpid()))

def thread_get(name,queue):
    print('start get %s:%s' % (name, os.getpid()))
    while not queue.empty():
        print('get from queue:%s'%queue.get())
    print('end get %s:%s' % (name, os.getpid()))

if __name__ == '__main__':
    print('main process start %s' % os.getpid())
    queue = Queue(maxsize=1000)
    thread_put = Thread(target=thread_put, args=('put',queue))
    thread_put.start()

    thread_get = Thread(target=thread_get, args=('put',queue))
    thread_get.start()
    # 成对出现，queue.join()之后会一直等待，需要调用task_done()来结束
    queue.task_done()
    queue.join()
    print('main prcess finish')