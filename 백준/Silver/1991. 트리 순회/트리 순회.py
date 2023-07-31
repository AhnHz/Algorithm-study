n = int(input())

node = {}

for i in range(n):
    root, left, right = input().split()
    node[root] = [left, right]      # left, right 노드를 해당 root키의 값으로 저장

node_key = list(node.keys())    # root가 될 수 있는 노드 저장

def preorder(root):
    print(root, end='')     # 1. root 노드 출력

    if node[root][0] != '.':    # left 노드가 있다면
        preorder(node[root][0])     # 2. left 노드가 root 노드가 되어 출력됨
    if node[root][1] != '.':    # right 노드가 있다면
        preorder(node[root][1])     # right 노드가 root 노드가 되어 출력됨

def inorder(root):
    if node[root][0] != '.':    # 1. 위 함수와 같지만, left 노드 먼저 출력
        inorder(node[root][0])

    print(root, end='')     # 2. root 노드 출력

    if node[root][1] != '.':    # 3. 위 함수와 같지만, right 노드 출력
        inorder(node[root][1])

def postorder(root):
    if node[root][0] != '.':    # 1. 위 함수와 같지만, left 노드 먼저 출력
        postorder(node[root][0])
    if node[root][1] != '.':
        postorder(node[root][1])    # 2. 위 함수와 같지만, right 노드 먼저 출력

    print(root, end='')     # 3. root 노드 출력

preorder(node_key[0])
print()
inorder(node_key[0])
print()
postorder(node_key[0])