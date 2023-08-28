def solution(n, lost, reserve):
    lost_uni = set(lost) - set(reserve)
    reserve_uni = set(reserve) - set(lost)
    
    for i in reserve_uni:
        if i - 1 in lost_uni:       # 앞번호 학생이 체육복이 없는 경우
            lost_uni.remove(i-1)    # 앞번호 학생은 체육복을 빌릴 수 있음
        
        elif i + 1 in lost_uni:     # 뒷번호 학생이 없는 경우
            lost_uni.remove(i+1)     
        
    return n - len(lost_uni)        # 전체 학생 - 체육복이 없는 학생