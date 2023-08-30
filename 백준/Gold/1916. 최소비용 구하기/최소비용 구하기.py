import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, d, c = map(int, sys.stdin.readline().split())
    graph[s].append((d, c))     # 목적지와 비용 추가

sta, desti = map(int, sys.stdin.readline().split())

distance = [float('inf')] * (N + 1)     # 최소 비용을 무한대로 초기화
distance[sta] = 0       # 출발지 비용 초기화

queue = [(0, sta)]     # 최소 비용과 노드 번호를 큐에 저장

while queue:
    dist, now = heapq.heappop(queue)    # 우선순위 큐에서 가장 적은 비용과 노드 번호 pop

    if distance[now] < dist:    # 찐 최소비용을 찾기 위해 무시
        continue

    for nxt, cost in graph[now]:    # 인접한 노드
        if distance[nxt] > dist + cost:     # 현재 노드를 거치는게 더 적다면
            distance[nxt] = dist + cost     # 현재 노드까지의 최소 비용을 갱신
            heapq.heappush(queue, (distance[nxt], nxt)) # 우선순위 큐에 인접 노드와 비용을 push

print(distance[desti])      # 출발지에서 도착지까지의 최소 비용
