def solution(n):
    answer = (pow(n, 0.5) +1)**2 if int(pow(n, 0.5)) == pow(n, 0.5) else -1
    
    return answer