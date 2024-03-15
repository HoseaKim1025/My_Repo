def generator():
    yield 1
    yield 'string'
    yield True
    

g = generator()

for _ in range(3):
    print(next(g))

# dd