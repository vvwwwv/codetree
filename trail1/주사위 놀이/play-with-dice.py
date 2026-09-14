arr = list(map(int, input().split()))
answer = [0 for _ in range(7)]
for i in arr:
    answer[i] += 1

for i in range(1,7):
    print(f"{i} - {answer[i]}")
