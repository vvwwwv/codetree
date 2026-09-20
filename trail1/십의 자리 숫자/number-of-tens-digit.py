arr = list(map(int, input().split()))
arr2 = []
for i in arr:
    if i == 0:
        break
    arr2.append(i)
answer = [0 for _ in range(10)]

for i in arr2:
    answer[i//10] += 1

for i in range(1, 10):
    print(f"{i} - {answer[i]}")