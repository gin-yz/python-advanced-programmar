"""
线程池,future可以要多线程和多进程编程接口一致
"""
import os
from concurrent.futures import ThreadPoolExecutor,as_completed
from time import sleep


def thread_pool_test(times):
    print('start {0} : {1}'.format(os.getpid(), times))
    sleep(times)
    print('end {0} : {1}'.format(os.getpid(), times))
    return 'return {0} : {1}'.format(os.getpid(), times)


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=5)
    # 直接传值，立马开始,返回future对象
    task1 = executor.submit(thread_pool_test, 2)
    task2 = executor.submit(thread_pool_test, 3)
    # result()方法返回线程执行值，会阻塞；done()方法判断是否完成（包括取消）

    print(task1.done())
    print(task2.done())


    # 只有未开始的进程可以被取消，取消后返回False
    print(task1.cancel())
    print(task2.cancel())

    print(task1.result())
    print(task2.result())
