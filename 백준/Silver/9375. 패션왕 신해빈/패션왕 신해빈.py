from collections import Counter

case = int(input())     # 테스트 케이스 수

for i in range(case):
    n = int(input())    # 조합할 수 있는 옷 개수
    cloth = []
    comb = 1

    for j in range(n):
        a, b = input().split()
        cloth.append(b)     # 옷 종류만 리스트에 저장

    cnt = Counter(cloth)    # 종류별 빈도수

    for key, value in cnt.items():
        comb *= value + 1       # 종류별 빈도수+1 곱하기

    print(comb-1)