n = int(input())

for i in range(n):
    ps = input()
    stack = []

    for j in ps:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:   # in stack True
                stack.pop()
            else:   # in stack nothing
                print('NO')
                break

    else:
        if stack:   # in stack True
            print('NO')
        else:   # in stack nothing. 다 pop 되었음
            print('YES')
