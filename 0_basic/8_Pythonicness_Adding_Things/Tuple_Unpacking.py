numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

# Switch Example
a = 1
b = 2
print("a=", a, " b=", b)
a, b = b, a
print("a=", a, " b=", b)


# Solve gcd
def gcd(x, y):
    while y:
        x, y = y, x % y  # Equals to y, (x % y)
    return x


print(gcd(256, 72))

# Use *(Asterisk)
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)
