import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 그래프 생성
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, d, c = map(int, sys.stdin.readline().split())
    graph[s].append((d, c))     # 목적지와 비용 추가

sta, desti = map(int, sys.stdin.readline().split())

distance = [float('inf')] * (N + 1)     # 최단 거리를 무한대로 초기화
distance[sta] = 0

queue = [(0, sta)]     # 최단 거리와 노드 번호를 큐에 저장

while queue:
    dist, now = heapq.heappop(queue)

    if distance[now] < dist:
        continue

    for nxt, cost in graph[now]:    # 인접한 노드
        if distance[nxt] > dist + cost:
            distance[nxt] = dist + cost
            heapq.heappush(queue, (distance[nxt], nxt))

print(distance[desti])