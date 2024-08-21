# Read Judge
try:
    file = open("test.txt", "r")
    print(file.read(16))
    print(file.read(4))
    print(file.read(4))
    print(file.read())
except:
    print("Fail to open the file")
    raise

# Close Method
try:
    file.close()
except:
    print("Fail to close the file")
