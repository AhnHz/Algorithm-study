n = int(input())
total = []

for i in range(n):
    a, b = map(int, input().split())
    total.append(a+b)
    
for i in total:
    print(i)