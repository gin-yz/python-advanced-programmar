"""
使用as_completed方法可以遍历出已经完成的方法,未完成的方法阻塞直到完成，返回future对象
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

    urls=[1,10,3,4]
    task_list = [executor.submit(thread_pool_test,url)for url in urls]
    print(task_list)

    for future in as_completed(task_list):
        print('main get return : {}'.format(future))

    # executor.map()直接返回result对象
    task_list2 = executor.map(thread_pool_test,urls)
    print(task_list2)
