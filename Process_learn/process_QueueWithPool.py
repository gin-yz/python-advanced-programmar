# 使用pool时，要使用Manager中的pool，不然报错
from multiprocessing import Manager, Pool
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
            print(queue.get(block=True, timeout=5))
    sleep(1)
    print('finish %s' % num)


if __name__ == '__main__':
    print('main process:%s' % os.getpid())
    # 指定队列大小，空则为无限
    queue = Manager().Queue(5)
    pool = Pool(processes=5)
    pool.apply(func=fuc_w, args=('write', queue))
    pool.apply(func=fuc_r, args=('read', queue))
    pool.close()
    pool.join()
