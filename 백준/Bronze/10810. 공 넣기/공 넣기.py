N, M = map(int, input().split())
basket = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())

    for i in range(i, j+1):
        basket[i-1] = k     # i번부터 j번 바구니에 k공 넣기

for i in basket:
    print(i, end=' ')