# 必须定义enter、exit魔法函数
class Sample:
    def __enter__(self):
        # 获取资源
        print('ether')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("exit")

    def do_someting(self):
        print('do something')


if __name__ == '__main__':
    with Sample() as sample:
        sample.do_someting()
