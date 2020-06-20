def gen_demo():
    word = yield "aaaa"

    print('inside:%s' % word)

    yield "ccc"

    yield "ddd"


gen = gen_demo()

print(next(gen))

print(gen.send('bbb'))

print(next(gen))
