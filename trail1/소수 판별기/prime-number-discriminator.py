n = int(input())
ck = True
for i in range(2, n+1):
    if n % i == 0 and n != i:
        ck = False
        break
    
if ck == True:
    print("P")
else:
    print("C")