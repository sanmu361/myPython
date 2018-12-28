# coding: utf-8 -*-


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield  b
        a, b = b, a + b
        n = n + 1

g = fib(7)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e)
        break