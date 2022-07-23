from datetime import datetime
import numpy as np
# concatenate


def method1():
    l = []
    for n in range(10000):
        l = l + [n]


def method2():
    l = []
    for n in range(10000):
        l.append(n)


def method3():
    l = [n for n in range(10000)]


def method4():
    l = list(range(10000))


start = datetime.timestamp(datetime.utcnow())
method1()
end = datetime.timestamp(datetime.utcnow())

print("\nThe Elapsed time: {:.2f} second".format((end - start)))

start = datetime.timestamp(datetime.utcnow())
method2()
end = datetime.timestamp(datetime.utcnow())

print("\nThe Elapsed time: {:.2f} second".format((end - start)))


start = datetime.timestamp(datetime.utcnow())
method3()
end = datetime.timestamp(datetime.utcnow())

print("\nThe Elapsed time: {:.2f} second".format((end - start)))

start = datetime.timestamp(datetime.utcnow())
method4()
end = datetime.timestamp(datetime.utcnow())

print("\nThe Elapsed time: {:.2f} second".format((end - start)))
