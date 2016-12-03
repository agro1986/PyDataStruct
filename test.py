from pydatastruct import *

print('hello')

l = LinkedList()
print(l.length)

l.add(10)
print(l.length)

l.add(20)
print(l.length)

for i in range(l.length):
    print(l.at(i))
