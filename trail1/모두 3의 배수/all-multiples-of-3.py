ck = True
for _ in range(5):
    a = int(input())
    if a % 3 != 0:
        ck = False
if ck == True:
    print(1)
else:
    print(0)