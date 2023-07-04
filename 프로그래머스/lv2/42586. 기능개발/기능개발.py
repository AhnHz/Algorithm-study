def solution(progresses, speeds):
    cnt = 0
    loop = 0
    answer = []
    
    while len(progresses) > 0:
        if (progresses[0] + loop * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            
        else:
            if cnt:
                answer.append(cnt)
                cnt = 0 
            loop += 1
    answer.append(cnt)       
    return answer
    
