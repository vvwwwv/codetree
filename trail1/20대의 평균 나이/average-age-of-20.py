sum, i = 0, 0
while 1:
    a = int(input())
    if a > 19 and a < 30:
        sum += a
        i+=1
    else:
        print(f"{sum/i:.2f}")
        break