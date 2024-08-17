def add(x, y):
	return x + y

def do_twice(function, x, y):
	return function( function(x, y), function(x, y) )

a = 5
b = 10
print(do_twice(add, x, y))

