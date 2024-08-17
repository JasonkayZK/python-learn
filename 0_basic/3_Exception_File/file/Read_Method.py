# Open Judge
try:
	file = open("test.txt", "r")
	cont = file.read()
	print(cont)
except:
	print("Fail to open the file")
	raise

# Close Judge
try:
	file.close()
except:
	print("Fail to close the file")
