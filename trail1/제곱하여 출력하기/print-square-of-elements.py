n = int(input())
arr1 = list(map(int, input().split()))
arr2 = [i * i for i in arr1]

for i in arr2:
    print(i, end=" ")