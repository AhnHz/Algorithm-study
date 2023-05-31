def solution(x):
    
    return bool(x % sum(map(int, str(x))) == 0)