word = input()
cnt = 0

while word:
    if word[:2] == 'c=' or word[:2] == 'c-' or word[:2] =='d-' or word[:2] == 'lj' or word[:2] == 'nj' or word[:2] == 's=' or word[:2] == 'z=':
        cnt += 1
        word = word[2:]

    elif word[:3] == 'dz=':
        cnt += 1
        word = word[3:]
    else:
        cnt += 1
        word = word[1:]

print(cnt)