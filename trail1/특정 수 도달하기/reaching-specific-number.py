arr = list(map(int, input().split()))
result = []
sum = 0
for i in arr:
    if i >= 250:
        break
    result.append(i)
    
for i in result:
    sum += i
print(f"{sum} {sum/len(result):.1f}")