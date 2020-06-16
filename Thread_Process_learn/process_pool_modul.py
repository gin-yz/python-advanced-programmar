# apply(同步，阻塞),apply_async(异步,非阻塞)
# 进程池满了之后要等待其他进程执行完毕
import os
from multiprocessing import Pool
from time import sleep


def func(num):
    print('子进程:%s' % os.getpid())
    print('process %s start' % num)
    sleep(1)
    print('process %s end' % num)

if __name__ == '__main__':
    pool = Pool(processes=3)
    for i in range(10):
        pool.apply_async(func=func,args=(i,))

    pool.close()

    pool.join()
