
def gen_fun():
    yield 1
    yield 2
    yield 3
    return "end"

if __name__ == '__main__':
    gen = gen_fun()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))