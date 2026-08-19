n = int(input())
a = 10
for i in range(n):
    for j in range(n):
        a-=1
        print(a, end="")
        if a == 1:
            a = 10
    print()