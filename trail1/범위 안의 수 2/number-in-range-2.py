sum, n = 0, 0
for i in range(10):
    a = int(input())
    if a >= 0 and a <= 200:
        sum += a
        n += 1
print(f"{sum} {sum/n:.1f}")
