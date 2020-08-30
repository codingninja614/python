def generatorfunction(num):
    for i in range(num):
        yield i*2
for item in generatorfunction(10):
    print(item)
g=generatorfunction(100)
next(g)
next(g)
print(next(g) )
