from collections import deque

size, num = map(int, input().split())
queue = deque([i for i in range(1, size+1)])  # 1~size

index = list(map(int, input().split()))  # 뽑는 위치

cnt = 0
for i in index:
    while(1):
        if queue[0] == i:
            queue.popleft()
            break

        idx = queue.index(i)  # 큐 회전시키면 index 순서가 꼬이므로 찾는 숫자의 index 다시 지목
        if idx <= len(queue) // 2:
            queue.rotate(-1)
            cnt += 1

        else:
            queue.rotate(1)
            cnt += 1

print(cnt)