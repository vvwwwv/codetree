arr = list(map(int, input().split()))
arr2 = []
for i in arr:
    if i == 0:
        break
    arr2.append(i)
for i in range(len(arr2)-1, -1, -1):
    print(arr2[i], end=" ")