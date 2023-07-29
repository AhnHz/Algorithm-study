arr = []

for i in range(9):
    n = int(input())
    arr.append(n)   # 입력받은 정수를 배열로 저장

print(max(arr), arr.index(max(arr))+1)  # 최대값과 최대값의 인덱스+1