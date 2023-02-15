height = 0

while height < 1 or height > 8:
    height = int(input("Height: "))

for i in range(1, height + 1):
    for space in range(height - i):
        print(" ", end="")
    for hash in range(i):
        print("#", end="")
    print("  ", end="")
    for hash in range(i):
        print("#", end="")
    print()

    

