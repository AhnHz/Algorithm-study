class ListNode:
    '''연결 리스트용 노드 클래스'''
    def __init__(self, u, d):
        '''초기화'''
        self.up = u if u >= 0 else None    # 윗 행
        self.down = d if d < N else None    # 아래 행

def solution(n, k, cmd):
    global N
    N = n
    
    # linked list
    table = {i: ListNode(i-1, i+1) for i in range(n)}  # 0 ~ n
    
    now = k  # 커서 위치
    delete = []  # 삭제한 행
    answer = ['O'] * n
    
    
    def move_down(X, now):        
        for _ in range(X):
            if table[now].down is not None:  # 아래 행이 존재함
                now = table[now].down
            else:  # down is None: 현재 행이 마지막 행
                while table[now].up is not None:  # up이 None이 아닐 경우
                    now = table[now].up  # 커서를 첫번째 행으로
        return now
            
    def move_up(X, now):        
        for _ in range(X):
            if table[now].up is not None:  # 윗 행이 존재함
                now = table[now].up
            else:   # up is None: 현재 행이 첫번째 행
                while table[now].down is not None:  # down이 None이 아닐 경우
                    now = table[now].down  # 커서를 마지막 행으로
        return now
    
    for command in cmd:
        if command == 'C':
            up, down = table[now].up, table[now].down
            delete.append(now)  # 삭제된 행 리스트에 추가
            
            if up is not None:
                table[up].down = down 
                
            else:  # up is None: 현재 행이 첫번째 행
                table[down].up = None  # 삭제된 후, 아래 행을 첫번째 행으로 설정
                
            if down is not None:
                table[down].up = up
                now = down  # 아래 행으로 커서 이동
                
            else:  # down is None: 현재 행이 마지막 행
                table[up].down = None  # 삭제된 후, 윗 행을 마지막 행으로 설정
                now = up  # 윗 행으로 커서 이동                         
                
        elif command == 'Z':
            z = delete.pop()  # 최근 삭제 행 반환 후, 삭제
            up, down = table[z].up, table[z].down
            
            if up is not None:
                table[up].down = z
                
            if down is not None:
                table[down].up = z
                
        else:  # U X, D X
            c, X = command.split()
            
            if c == 'U':
                now = move_up(int(X), now)
            else:  # 'D'
                now = move_down(int(X), now)
     
    for x in delete:
        answer[x] = 'X'  # 삭제된 행을 인덱스로 찾아 'X'로 변경
                          
    return ''.join(answer)