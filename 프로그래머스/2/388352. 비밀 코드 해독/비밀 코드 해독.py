from itertools import combinations

def solution(n, q, ans):
    secret_code = list(combinations(range(1,n+1), 5)) # n까지의 정수 5개
    
    cnt = 0
    
    for i in secret_code:
        for idx, val in enumerate(q):
            if len(set(i) & set(val)) != ans[idx]:
                break
        else:            
            cnt+=1 # 조건에 부합하는 비밀코드면 카운트
        
    return cnt