#coding=utf-8
l1 = list(range(1,11))

print(l1)

l2 = []
for x in range(1,11):
    l2.append(x * x)
print(l2)

l3 = [x * x for x in range(1,11)]

print(l3)

l4 = [x * x for x in range(1,11) if x % 2 == 0]
print(l4)

l5 = [m + n for m in 'ABC' for n in 'XYZ']
print(l5)

import os
l6 = [d for d in os.listdir('.')]

print(l6)

l7 = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in l7.items():
    print(k,"=",v)