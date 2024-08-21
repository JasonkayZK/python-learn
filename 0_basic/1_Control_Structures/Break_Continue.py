i = 0  # Circulation Variaty
while True:
    i = i + 1
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("Breaking!")
        break
    print(i)  # This print is in the circulation!

print("Finished!")
