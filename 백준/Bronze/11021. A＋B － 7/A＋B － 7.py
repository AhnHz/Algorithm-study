n = int(input())
sum = []

for i in range(n):
    a, b = map(int, input().split())
    sum.append(a+b)

for i, s in enumerate(sum):
    print('Case #{}: {}'.format(i+1, s))