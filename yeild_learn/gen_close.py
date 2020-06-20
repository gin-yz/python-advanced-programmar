def gen_demo():
    yield "aaaa"

    yield "ccc"

    yield "ddd"


gen = gen_demo()

print(next(gen))

gen.close()

print(next(gen))
