import sys

n, c = map(int, sys.stdin.readline().split())   # input 대신 sys.stdin.readline
num = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(n-1):
    for j in range(n-1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
            cnt+=1

            if cnt == c:
                print(num[j], num[j+1])
                quit()

print(-1)