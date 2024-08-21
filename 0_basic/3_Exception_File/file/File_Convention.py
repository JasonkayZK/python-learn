try:
    f = open("test.txt")
    print(f.read())
finally:
    f.close()
