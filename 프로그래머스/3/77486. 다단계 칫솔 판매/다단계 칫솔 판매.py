class Node:
    def __init__(self, r, plus):
        self.up = r
        self.profit = plus
        self.money = [0]

        
def solution(enroll, referral, seller, amount):
    # linked list
    tree = {n: Node(r, 0) for n, r in zip(enroll, referral)}
    answer = []
    
    for i in range(len(seller)):  # 0 ~ seller num
        ten = 1
        #print('index: ', i)
        #print('판매원: ', seller[i])
        now = seller[i]
        amount[i] *= 100  # 하나당 100원
        a = amount[i]
        
        while ten:
            ten = a // 10  # 첫번째 분배
            own = a - ten  # 10% 뗀 자신의 몫
            #print('  now: ', now)
            money = tree[now].money
            money.append(own)

            up = tree[now].up
            
            if up == '-':  # 추천인이 센터인 경우       
                break
                
            tree[up].profit += ten  # 추천인 10% 수수료
            
            
            #print('  추천인: ', up)
            #print('  수수료: ', ten)
            #print('  자신의 몫: ', own)
            
            now = up
            a = ten
            
        #print(seller[i], '이익: ', tree[seller[i]].money)
        #print('-' * 20)
            
    for i in enroll:
        money = tree[i].money
  
        total = sum(money)
        #print('{}의 수익: {}'.format(i, total))
        answer.append(total)
        
    return answer