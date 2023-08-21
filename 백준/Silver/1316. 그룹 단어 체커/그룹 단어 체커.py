n = int(input())
cnt = 0

for i in range(n):      
    word = input()
    group = True

    for j in range(len(word)-1):    # 문자열 순회
        if word[j] != word[j + 1] and word[j + 1] in word[:j + 1]:  # 앞 문자와 다른데 이전에 나온 문자와 같다면
            group = False   # 그룹 단어가 아니다
            break

    if group:
        cnt += 1    # 그룹 단어 카운트

print(cnt)