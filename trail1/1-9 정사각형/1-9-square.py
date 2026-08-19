n = int(input())
a = 0
for i in range(n):
    for j in range(n):
        a+=1
        print(a, end="")
        if a == 9:
            a = 0
    print()