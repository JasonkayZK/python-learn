def my_func(x, y = 7, *args, **kwargs):
	print(args)
	print(kwargs)

my_func(2, 3, 4, 5, 6, a = 7, b = 8)


