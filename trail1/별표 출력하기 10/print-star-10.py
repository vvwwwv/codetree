n = int(input())
a, b = 1, n
for i in range(n*2):
    if i % 2 == 0:
        for j in range(a):
            print("*", end=" ")
        a += 1
    else:
        for j in range(b):
            print("*", end=" ")
        b -= 1
    print()