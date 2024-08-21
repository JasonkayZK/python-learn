from itertools import cycle

mylist = [1, 2, 3, 4, 5]
for i in cycle(mylist):
    print(mylist)
    if i > 3:
        break

mylist = [2, 3, 4, 5, 6]
for i in cycle(mylist):
    print(mylist)
    if i > 3:
        break
