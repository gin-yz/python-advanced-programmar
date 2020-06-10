# 私有属性，前面加__，但还是可以通过_类名访问，没有绝对的安全
class Test(object):
    """
    __doc__显示
    和和
    """
    def __init__(self, brithday):
        self.__brithday = brithday

    def __str__(self):
        return self.__brithday


if __name__ == '__main__':
    test = Test('aaaa')
    print(test)
    print(test.__brithday)
    print(test._Test__brithday)
