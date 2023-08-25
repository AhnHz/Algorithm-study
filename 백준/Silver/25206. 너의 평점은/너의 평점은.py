grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
total = 0
mulsum = 0

for i in range(20):
    sub, sco, gra = input().split()
    sco = float(sco)    # 평점은 실수로 변환

    if gra != 'P':  # P가 아니라면 계산
        total += sco    # 학점 총합
        mulsum += sco * score[grade.index(gra)]  # 학점 * 과목평점   

print('{:.6f}'.format(mulsum/total))