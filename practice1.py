n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print("*", end="")

    for j in range(i - 1):
        print("*", end="")

    print()5