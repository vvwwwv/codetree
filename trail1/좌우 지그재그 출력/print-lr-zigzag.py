n = int(input())
cnt_s = 0
cnt_e = 0
for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            cnt_s += 1
            print(cnt_s, end=" ")
        cnt_e = cnt_s + n
        cnt_s = cnt_e
        print()
    else:
        for j in range(n):
            print(cnt_e, end=" ")
            cnt_e -= 1
        print()