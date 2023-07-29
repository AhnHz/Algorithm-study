n, x = map(int, input().split())
arr = input().split()
under = []

for i in range(n):  # for문 돌릴 필요는 없지만 문제에 정수 개수를 입력받는게 있기 때문에
    arr[i] = int(arr[i])
    if arr[i] < x:
        #under.append(arr[i])
        print(arr[i])