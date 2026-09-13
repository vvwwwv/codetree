n = int(input())
arr = [0 for i in range(10)]
inArr = list(map(int, input().split()))

for i in inArr:
    arr[i] += 1

for i in range(1, 10):
    print(arr[i])