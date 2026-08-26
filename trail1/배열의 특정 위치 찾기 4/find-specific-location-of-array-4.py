arr = list(map(int, input().split()))
arr2 = []
cnt = 0
for i in arr:
    if i == 0:
        break
    if i % 2 == 0:
        cnt += 1
        arr2.append(i)
print(f"{cnt} {sum(arr2)}")