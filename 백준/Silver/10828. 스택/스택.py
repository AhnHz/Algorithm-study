import sys

n = int(input())    # 명령어 개수 입력 
stack = []

def push(x):
    stack.append(x)     # 스택에 추가

def top():
    if len(stack) == 0:
        print(-1)   # 스택이 비어있으면 -1 출력
    else: print(stack[-1])  # 최상단 요소 출력

def size():
    print(len(stack))   # 스택 사이즈 출력

def empty():
    if len(stack) == 0:
        print(1)    # 스택이 비어있으면 1(참) 출력
    else: print(0)

def popf():
    if len(stack) == 0:
        print(-1)   # 스택이 비어있으면 -1 출력(반환할 요소가 없음)
    else: print(stack.pop())    # 최상단 요소 pop 


for i in range(n):
    com = sys.stdin.readline().split()  # n개의 명령 입력받기

    if com[0] == 'push':
        push(int(com[1]))

    elif com[0] == 'top':
        top()

    elif com[0] == 'size':
        size()   

    elif com[0] == 'empty':
        empty()

    elif com[0] == 'pop':
        popf()
