num = list(range(1, 31))    # 1~30 번

for i in range(28):
    submit = int(input())

    if submit in num:
        num.remove(submit)      # 제출한 학생 출석번호를 리스트에서 삭제

for i in num:
    print(i)