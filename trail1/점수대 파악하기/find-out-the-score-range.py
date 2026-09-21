arr = list(map(int, input().split()))
arr2 = []
for i in arr:
    if i == 0:
        break
    arr2.append(i)

answer = [0 for i in range(11)]

for i in arr2:
    answer[i//10] += 1

for i in range(10,0,-1):
    print(f"{i}0 - {answer[i]}")