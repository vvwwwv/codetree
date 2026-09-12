n = int(input())
arr = [1, n]
i = 2
while 1:
    arr.append(arr[i-1] + arr[i-2])
    if arr[i-1] + arr[i-2] > 100:
        break
    i+=1
print(*arr)