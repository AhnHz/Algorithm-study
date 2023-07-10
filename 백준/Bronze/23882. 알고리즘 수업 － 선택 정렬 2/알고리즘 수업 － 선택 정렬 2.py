n, c = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0

for i in range(n-1, 0, -1): # 역순
    if num[i] < max(num[:i]):
        num[i], num[num.index(max(num[:i]))] = num[num.index(max(num[:i]))], num[i]
        cnt += 1
        if cnt == c:
            sorted_num = " ".join(str(s) for s in num)
            print(sorted_num)
            quit()

print(-1)