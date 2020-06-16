from multiprocessing import Process, Queue
import os
from time import sleep


def fuc_w(num, queue):
    print('start {0}:{1}'.format(num, os.getpid()))
    for i in range(5):
        queue.put(i)
    sleep(1)
    print('finish %s' % num)


def fuc_r(num, queue):
    print('start {0}:{1}'.format(num, os.getpid()))
    if not queue.empty():
        for i in range(queue.qsize()):
            #block = True表示非阻塞，timeout=5表示等5s
            print(queue.get(block=True, timeout=5))
    sleep(1)
    print('finish %s' % num)


if __name__ == '__main__':
    print('main process:%s' % os.getpid())
    # 指定队列大小，空则为无限
    queue = Queue(5)
    pw = Process(target=fuc_w,args=('read',queue))
    pr = Process(target=fuc_r,args=('write',queue))
    pw.start()
    pr.start()
    pr.join()
