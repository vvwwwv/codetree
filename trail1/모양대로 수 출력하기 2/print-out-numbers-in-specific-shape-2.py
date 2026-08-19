n = int(input())
a = 0
for i in range(n):
    for j in range(n):
        a+=2
        print(a, end=" ")
        if a == 8:
            a = 0
    print()