import sys

n = int(input())
stack = []

def push(x):
    stack.append(x)

def top():
    if len(stack) == 0:
        print(-1)
    else: print(stack[-1])

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else: print(0)

def popf():
    if len(stack) == 0:
        print(-1)
    else: print(stack.pop())


for i in range(n):
    com = sys.stdin.readline().split()

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