import sys
import heapq

heap = []
n = int(input())

for _ in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(heap, x)
    else:  # x == 0
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))