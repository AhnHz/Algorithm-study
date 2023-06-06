def solution(n, lost, reserve):
    
    lost_uni = set(lost) - set(reserve)
    reserve_uni = set(reserve) - set(lost)
    
    for i in reserve_uni:
        if i - 1 in lost_uni:
            lost_uni.remove(i-1)
        
        elif i + 1 in lost_uni:
            lost_uni.remove(i+1)            
        
    return n - len(lost_uni) 