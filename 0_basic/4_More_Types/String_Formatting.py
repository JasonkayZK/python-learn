# string formatting
num = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(num[0], num[1], num[2])

print(msg)

numstr = ["one", "two", "three"]
msg = "Numbers: {0} {1} {2}".format(numstr[0], numstr[1], numstr[2])

print(msg)

a = "{x}, {y}".format(x = 5, y = 12)
print(a)

