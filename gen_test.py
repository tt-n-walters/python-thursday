
def naive_function():
    pies = []

    for _ in range(100000000):
        pies.append("3.141")
    
    return pies


def lazy_function():
    n = 0
    while n < 100000000:
        yield 3.141
        n += 1

pies = lazy_function()
# converted = map(float, pies)
print(sum(pies))