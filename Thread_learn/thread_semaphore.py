"""
用于控制进入数量的锁
"""

import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, mutex):
        super().__init__()
        self.url = url
        self.mutex = mutex

    def run(self):
        time.sleep(2)
        print("got html text success:{}".format(self.url))
        self.mutex.release()


class UrlProducer(threading.Thread):
    def __init__(self, mutex):
        super().__init__()
        self.mutex = mutex

    def run(self):
        for i in range(20):
            self.mutex.acquire()
            html_thread = HtmlSpider("https://baidu.com/{}".format(i), self.mutex)
            html_thread.start()


if __name__ == "__main__":
    # 多少个资源
    mutex = threading.Semaphore(3)
    url_producer = UrlProducer(mutex)
    url_producer.start()
