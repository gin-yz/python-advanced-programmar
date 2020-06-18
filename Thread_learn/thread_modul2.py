# 继承Thread实现,重写run方法
import os
from threading import Thread
from time import sleep


class thread_demo(Thread):
    def __init__(self, name, hehe, daemon):
        super().__init__(name=name, daemon=daemon)
        self.hehe = hehe

    def run(self):
        print('start %s:%s' % (self.name, os.getpid()))
        print(self.hehe)
        sleep(2)
        print('end %s:%s' % (self.name, os.getpid()))


if __name__ == '__main__':
    print('main process start %s' % os.getpid())
    thread1 = thread_demo('cjs', hehe='hehe', daemon=True)
    thread1.start()
    thread1.join()
    print('main prcess finish')
