a, b = map(int, input().split())

count = [0] * b

while a > 1:
    r = a % b
    count[r] += 1
    a //= b
answer = 0
for c in count:
    answer += c * c

print(answer)