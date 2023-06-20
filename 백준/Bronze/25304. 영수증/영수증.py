rec = int(input())
n = int(input())
total = 0

for i in range(n):
    price, num = map(int, input().split())
    total += price * num
    
print('Yes' if rec == total else 'No')