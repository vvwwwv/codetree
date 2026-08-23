n = int(input())
arr = list(map(float, input().split()))
sum = sum(arr)
print(f"{sum/n:.1f}")
if sum / n >= 4:
    print("Perfect")
elif sum / n >= 3:
    print("Good")
else:
    print("Poor")