def solution(n, w, num):
    ly, lx = divmod(n, w) # last box
    sy, sx = divmod(num, w) # standard box
    
    if lx == 0:
        ly -= 1
        lx = w
    if sx == 0:
        sy -= 1
        sx = w
        
    if w == 1:
        return (n-num) + 1
        
    answer = ly - sy
    
    if ly%2 == sy%2: # 마지막 상자와 기준 상자의 정리 순서가 같을 경우
        if lx < sx:
            answer-=1
        
    else: # 마지막 상자와 기준 상자의 정리 순서가 다를 경우
        if (w-lx) >= sx:
            answer-=1
            
    return answer+1