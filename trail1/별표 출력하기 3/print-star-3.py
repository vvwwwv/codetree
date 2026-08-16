n = int(input())
for i in range(n*2-1, 0, -2):
    for j in range(n*2-1-i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()