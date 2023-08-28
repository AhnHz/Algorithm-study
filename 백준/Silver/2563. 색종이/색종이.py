n = int(input())
papper = [[0] * 100 for _ in range(100)]  # 100 x 100
area = 0

for _ in range(n):
    x, y = map(int, input().split())    # 색종이 시작점 좌표

    for i in range(x, x+10):    # 색종이 밑변 길이
        for j in range(y, y+10):    # 색종이 높이 길이
            papper[i][j] = 1    # 0을 1로 바꾸면서 칠한다

for _ in range(100):
    area += papper[_].count(1)  # 도화지 위부터 1이 칠해진 넓이를 더한다

print(area)