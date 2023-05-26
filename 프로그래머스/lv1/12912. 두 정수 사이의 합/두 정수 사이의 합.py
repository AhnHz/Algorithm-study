def solution(a, b):
    answer = 0
    m = min(a,b)
    
    for i in range(abs(a-b)+1):
         
        answer += m
        m += 1
            
    return answer