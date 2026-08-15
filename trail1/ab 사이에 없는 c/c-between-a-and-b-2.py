a, b, c = map(int, input().split())
ck = True
for i in range(a, b+1):
    if i % c == 0:
        ck = False
        break
if ck == True:
    print("YES")
else:
    print("NO")