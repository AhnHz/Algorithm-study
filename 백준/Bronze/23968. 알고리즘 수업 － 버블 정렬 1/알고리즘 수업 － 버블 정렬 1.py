n, c = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0

for i in range(n-1):    # 자릿수마다 반복
    for j in range(n-1):    # 처음부터 끝까지 교환 한번씩
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
            cnt+=1      # 교환횟수 카운트
            if cnt == c:
                print(num[j], num[j+1])
                quit()

print(-1)