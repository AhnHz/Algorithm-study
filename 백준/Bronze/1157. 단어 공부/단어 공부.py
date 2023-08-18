from collections import Counter

string = list(input().upper())
most_str = Counter(string).most_common()    # 빈도수 별로 묶기, 정렬
maximum = most_str[0][1]    # 가장 높은 빈도수 중 첫값

if len([i for i in most_str if i[1] == maximum]) > 1:   # 빈도수가 maximum과 같은 값이 2개 이상인 경우
    print('?')

else: print(most_str[0][0])