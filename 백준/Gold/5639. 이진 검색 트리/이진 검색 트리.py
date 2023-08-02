import sys
sys.setrecursionlimit(10**6)

node_list = []

while 1:
    try:
        n = int(input())
        node_list.append(n)
    except:
        break

def postorder (node_list):
        if not node_list:    # node_list에 속한 노드여야함
            return

        root = node_list[0]
        left = [n for n in node_list[1:] if n < root]   # root 보다 작은 노드
        right = [n for n in node_list[1:] if n > root]   # root 보다 큰 노드

        #print('left: ', left)
        #print('right: ', right)
        #print('root: ', root)
        #print('-'* 20)
        postorder(left)
        postorder(right)

        print(root)

postorder(node_list)