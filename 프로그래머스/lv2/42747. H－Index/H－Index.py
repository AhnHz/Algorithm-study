def solution(citations):
    citations.sort(reverse=True)    # 내림차순 정렬

    for i in range(len(citations)):
        if citations[i] <  i+1:    # 인덱스가 요소값 이상인지
            return i     
        
    return len(citations)   # 모든 논문의 인용 횟수가 같은 경우
