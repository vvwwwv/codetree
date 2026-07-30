def sqr(n):
    a = 1
    for i in range(n):
        
        for j in range(n):
            print(a, end=" ")
            if a == 9: a = 0
            a += 1
        print()

a = int(input())
sqr(a)