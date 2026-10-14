arr = ["L", "E", "B", "R", "O", "S"]
a = input()
idx = -1

# 문자 탐색
for i in range(len(arr)):
    if arr[i] == a:
        idx = i

if idx == -1:
    print("None")
else:
    print(idx)