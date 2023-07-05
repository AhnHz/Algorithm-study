def solution(progresses, speeds):
    cnt = 0     # 개발된 기능 개수
    loop = 0    # 시간
    answer = []
    
    while len(progresses) > 0:
        if (progresses[0] + loop * speeds[0]) >= 100:   # 진도율 업
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            
        else:
            if cnt:
                answer.append(cnt)  # 개발된 기능이 있다면 정답 리스트에 개수 추가
                cnt = 0     # 개수 초기화
            loop += 1   # day + 1
    answer.append(cnt)  # 마지막 개발 완료       
    return answer