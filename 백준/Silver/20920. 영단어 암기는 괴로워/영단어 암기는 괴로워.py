import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())

word = [sys.stdin.readline().strip() for i in range(n)]
word = [i for i in word if len(i) >= m]

fre_word = Counter(word)
fre_word = sorted(fre_word.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))
#print(fre_word)

for i in fre_word:
    print(i[0])