# Open Judge
try:
    file = open("test.txt", "w")
    # do stuff to the file
except:
    print("Fail to open")

# Close Judge
try:
    file.close()
except:
    print("Fail to close")
