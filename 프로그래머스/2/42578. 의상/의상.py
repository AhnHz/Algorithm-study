from collections import Counter

def solution(clothes):
    answer = 1
    table = []
    
    for i in clothes:
        table.append(i[1])
    
    num = Counter(table)
    for key, val in num.items():
        answer *= (val+1)
    
    return answer - 1