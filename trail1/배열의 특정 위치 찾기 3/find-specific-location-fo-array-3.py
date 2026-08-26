arr = list(map(int, input().split()))
arr2 = []
for i in arr:
    if i == 0:
        break
    arr2.append(i)

sum = arr2[-1] + arr2[-2] + arr2[-3]
print(sum)