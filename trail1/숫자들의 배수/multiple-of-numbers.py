n = int(input())
i = 0
k = 0
while k < 2:
    i+=1
    print(i*n, end=" ")
    if (i*n) % 5 == 0:
        k+=1