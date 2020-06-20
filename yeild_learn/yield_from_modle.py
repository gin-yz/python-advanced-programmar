def g1(iterable):
    yield iterable


def g2(iterable):
    yield from iterable


for value in g1(range(10)):
    print(value)

for value in g2(range(10)):
    print(value)

#
def g3():
    x = yield
    print(x)
    yield
    return "hehe"


def g4():
    x = yield from g3()
    print('g4:{}'.format(x))

def g5():
    m = g4()
    next(m)
    m.send('g5 msg')
    m.send(None)
g5()