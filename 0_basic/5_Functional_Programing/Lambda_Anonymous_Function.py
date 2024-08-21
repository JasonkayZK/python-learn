def my_func(f, arg):
    return f(arg)


result = my_func(lambda x: 2 * x * x, 5)
print(result)


# Named function
def polynomial(x):
    return x**2 + 5 * x + 4


print(polynomial(-4))

# Lambda
print((lambda x: x**2 + 5 * x + 4)(-4))


# Assignment
double = lambda x: x * 2
print(double(7))
