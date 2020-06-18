"""
条件变量，用于复杂的线程间同步,完成协同,两种方法都可以
"""
from threading import Condition, Thread


class TianMao(Thread):
    def __init__(self, cond):
        super().__init__(name='天猫精灵')
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print('{}:在'.format(self.name))
            self.cond.notify()
            self.cond.wait()
            print('{}:好啊'.format(self.name))
            self.cond.notify()

class XiaoAI(Thread):
    def __init__(self, cond):
        super().__init__(name='小爱同学')
        self.cond = cond

    def run(self):
        self.cond.acquire()

        print('{}:天猫精灵'.format(self.name))
        self.cond.notify()
        self.cond.wait()
        print('{}:我们来对古诗吧'.format(self.name))
        self.cond.notify()
        self.cond.wait()

        self.cond.release()

if __name__ == '__main__':
    condition = Condition()
    tianmao_thread = TianMao(condition)
    xiaoai_thread = XiaoAI(condition)

    tianmao_thread.start()
    xiaoai_thread.start()

    tianmao_thread.join()
    xiaoai_thread.join()
