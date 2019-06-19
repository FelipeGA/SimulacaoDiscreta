import simpy

def lista_elementos ():
    i = 0
    yield i
    i = 1
    yield i
    i = 2
    yield i

l = lista_elementos()
print(next(l))
print(next(l))
print(next(l))
