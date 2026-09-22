arr = [0 for i in range(4)]
for i in range(3):
    a, b = input().split()
    b = int(b)
    if a == 'Y' and b >= 37:
        arr[0] += 1
    elif a == 'N' and b >= 37:
        arr[1] += 1
    elif a == 'Y' and b < 37:
        arr[2] += 1
    else:
        arr[3] += 1

print(*arr, end=" ")
if arr[0] >= 2:
    print("E")