arr = list(map(int, input().split()))
sum1 = arr[::2]
sum2 = arr[1::2]
sum1 = sum(sum1)
sum2 = sum(sum2)
if sum1 > sum2:
    print(sum1-sum2)
else:
    print(sum2-sum1)