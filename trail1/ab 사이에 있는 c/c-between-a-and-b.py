a, b, c = map(int, input().split())
ck = False
for i in range(a, b+1):
    if i % c == 0:
        ck = True
        break
if ck == False:
    print("NO")
else:
    print("YES")