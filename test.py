from pydatastruct import *

print('hello')

l = LinkedList()
print(l.length)

l.add(10)
print(l.length)

l.add(20)
print(l.length)

print()

for i in range(l.length):
    print(l.at(i))

print()

print(l.index_of(20))
print(l.index_of(1))

print()

for i in l:
    print(i)
