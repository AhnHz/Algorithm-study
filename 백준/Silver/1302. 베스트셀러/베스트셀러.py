import sys
from collections import Counter

n = int(sys.stdin.readline())
book = [sys.stdin.readline().strip() for i in range(n)]
#print(book)

top1 = Counter(book).most_common(1)     # 판매량이 가장 많은 요소 한개
#print(top1)

best = [i for i in set(book) if book.count(i) == top1[0][1]]    # 가장 많은 판매량과 판매부수가 같은 책만

print(sorted(best)[0])     # 사전순으로 정렬