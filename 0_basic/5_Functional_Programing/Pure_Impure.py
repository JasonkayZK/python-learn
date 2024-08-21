# Pure function:
def pure_function(x, y):
    temp = x + 2 * y
    return temp / (2 * x + y)


# Impure function:
some_list = []


def impure(arg):
    some_list.append(arg)
