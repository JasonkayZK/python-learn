from itertools import permutations, product

letters = ("A", "B")

print(list(product(letters, range(2))))
print(list(permutations(letters)))
