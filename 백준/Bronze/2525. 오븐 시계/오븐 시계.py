a,b = map(int, input().split())
c = int(input())

h = (c+b) // 60
b = (c+b) % 60

print((a+h)%24, b)