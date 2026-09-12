n, m = map(int, input().split())
arr = [n, m]
i = 2
while i<10:
    arr.append(arr[i-1] + 2*arr[i-2])
    i+=1
print(*arr)