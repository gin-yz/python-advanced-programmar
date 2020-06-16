# 通过Thread类实例化

from threading import Thread
import os
from time import sleep


def thread_demo(name):
    print('start %s:%s' % (name, os.getpid()))
    sleep(2)
    print('end %s:%s' % (name, os.getpid()))


if __name__ == '__main__':
    print('main process start %s' % os.getpid())
    # deamon = true表示主进程不等待线程执行完毕就退出，默认为False
    # thread1 = Thread(target=thread_demo, args=('cjs',),daemon=True)
    thread1 = Thread(target=thread_demo, args=('cjs',))
    thread1.start()
    # 主进程会等待thread1运行完后，再运行之后的
    thread1.join()

    print('main prcess finish')
