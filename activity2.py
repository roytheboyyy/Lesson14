n = int(input("enter number of row"))
num = 1
for i in range(n):
    for j in range(i+1):
        print(num , end="")
        num = num + 1
    print()