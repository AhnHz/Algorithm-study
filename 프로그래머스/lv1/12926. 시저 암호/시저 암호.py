def solution(s, n):
    sl = list(s)
    
    for i in range(len(sl)):
        if sl[i].isupper():
            sl[i] = chr((ord(sl[i]) - ord('A') +n) % 26 + ord('A'))
            
        elif sl[i].islower():
            sl[i] = chr((ord(sl[i]) - ord('a') +n) % 26 + ord('a'))
    
    
    return ''.join(sl)