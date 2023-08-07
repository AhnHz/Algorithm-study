import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())

word = [sys.stdin.readline().strip() for i in range(n)]
word = [i for i in word if len(i) >= m]     # m보다 짧은 단어 제외

fre_word = Counter(word)
#print(fre_word)
fre_word = sorted(fre_word.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))
# 빈도 내림차순, 길이 내림차순, 문자열 오름차순 정렬
#print(fre_word)

for i in fre_word:
    print(i[0])    # 단어만 출력