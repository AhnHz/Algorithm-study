class Node:
    def __init__(self, r):
        self.up = r
        self.money = [0]  # 수익
        
def solution(enroll, referral, seller, amount):
    # linked list
    tree = {n: Node(r) for n, r in zip(enroll, referral)}  # {판매원: 추천인}
    answer = []
    
    for i in range(len(seller)):
        now = seller[i]
        
        ten = 1  # 수수료 계산할 변수
        amount[i] *= 100  # 하나당 100원
        a = amount[i]
        
        while ten:  # 10% 뗄 수수료가 존재한다면
            ten = a // 10  # 10% 수수료
            own = a - ten  # 10% 뗀 자신의 몫(수익)
            money = tree[now].money
            money.append(own)

            up = tree[now].up            
            if up == '-':  # 추천인이 센터인 경우 수수료 분배 계산 생략     
                break
                            
            now = up
            a = ten
            
    for i in enroll:
        money = tree[i].money
        total = sum(money)  # 판매원마다 수익 총합
        answer.append(total)
        
    return answer