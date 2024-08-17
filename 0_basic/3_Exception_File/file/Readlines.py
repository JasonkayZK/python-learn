file = open("test.txt", "r")
print(file.readlines())
file.close()

# Use for ... in ... clause
file = open("test.txt", "r")

for line in file:
	print(line)
file.close()
