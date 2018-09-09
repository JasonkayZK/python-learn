def countdown():
	i = 5
	while i > 0:
		yield i
		i -= 1

result = list(countdown())
print(result)
for i in result:
	print(i)
