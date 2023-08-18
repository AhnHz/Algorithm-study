N = int(input())
score = list(map(int, input().split()))
max_score = max(score)
new_score = []

for s in score:
    new_score.append(s/max_score*100)

print(sum(new_score)/N)