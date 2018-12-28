
# -*- coding: utf-8 -*-
def hello(greeting, *args):
    if(len(args) == 0):
        print("%s!" % greeting)
    else:
        print('%s ，%s' % (greeting,','.join(args)))


hello('Hi')
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')