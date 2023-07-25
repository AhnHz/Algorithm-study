def solution(phone_book):
    phone_book.sort()   # 오름차순 정렬. 인접한 전화번호끼리만 비교하면 됨
    
    for i in range(len(phone_book)-1):
        # 기준이 되는 전화번호와 그 다음 전화번호 앞자리를 비교
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False    # 참이면 false를 반환하고 종료
            
    return True