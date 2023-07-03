n = int(input())
sum = []
num = []

for i in range(n):
    a, b = map(int, input().split())
    num.append(a)
    num.append(b)
    sum.append(a+b)

index = 0
for i, s in enumerate(sum):
    print('Case #{}: {} + {} = {}'.format(i+1, num[index], num[index+1], s))
    index += 2