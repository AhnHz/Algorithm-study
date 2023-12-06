from collections import Counter

def solution(clothes):
    answer = 1
    
    num = Counter(cat for cloth, cat in clothes)    # 종류별 빈도 계산
    
    for key, val in num.items():
        answer *= (val+1)   # 모든 경우의 수 - 1(0개 입는 경우)
    
    return answer - 1