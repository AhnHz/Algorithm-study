import heapq

def solution(scoville, K):
    cnt = 0
    heap = []
    
    for i in scoville:
        heapq.heappush(heap, i)
    
    while heap[0] < K:
        if len(heap) < 2:
            return -1
            
        new = heapq.heappop(heap) + heapq.heappop(heap) * 2  # 재료로 쓰인 두 음식 삭제
        heapq.heappush(heap, new)  # 새로운 음식 push
        cnt += 1
        
    if max(heap) < K:
        cnt = -1

    return cnt