a, b = map(int, input().split())

print(f"{a//b}.", end="")
for i in range(20):
    a = a % b
    print((a*10)//b, end="")
    a = (a*10) % b
