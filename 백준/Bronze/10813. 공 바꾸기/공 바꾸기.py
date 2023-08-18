N, M = map(int, input().split())
basket = [i+1 for i in range(N)]    # 바구니 번호와 같은 값 삽입

for _ in range(M):
    i, j = map(int, input().split())

    # i번 바구니와 j번 바구니의 값 바꾸기
    temp = basket[i-1]
    basket[i - 1] = basket[j-1]
    basket[j - 1] = temp

for i in basket:
    print(i, end=' ')