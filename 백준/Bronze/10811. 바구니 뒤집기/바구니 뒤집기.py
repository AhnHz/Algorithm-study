N, M = map(int, input().split())

basket = [i+1 for i in range(N)]

for m in range(M):
    i, j = map(int, input().split())

    basket[i-1:j] = reversed(basket[i-1:j])     # i번부터 j번까지 역순해서 다시 저장

for i in basket:
    print(i, end=' ')