# a list comprehension
cubes = [i ** 3 for i in range(5)]

print(cubes)

evens = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]

print(evens)

even = [2 * i for i in range(10 ** 100)]


