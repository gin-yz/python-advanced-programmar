# 类继承Process后重写run方法
import os
from multiprocessing import Process


class ChildProcess(Process):
    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        print('子进程:%s' % os.getpid())
        print(self.interval)
        print(locals())
        print('子进程终止')

if __name__ == '__main__':
    p = ChildProcess(2)
    p.start()
