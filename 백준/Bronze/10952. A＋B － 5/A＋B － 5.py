ans = []

while 1:
    a, b = map(int, input().split())

    if a == 0 & b == 0:
        break
    ans.append(a + b)

print(*ans, sep='\n')
