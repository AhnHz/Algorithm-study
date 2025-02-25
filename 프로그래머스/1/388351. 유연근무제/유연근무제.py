def solution(schedules, timelogs, startday):
    
    def time_calculator(time10): # 10진법 -> 60진법 변환
        hour = time10 // 100
        minute = time10 % 100
        return hour*60 + minute
    
    def all_smaller(lst, x): # timelogs[i], schedules[i]
        x = time_calculator(x) + 10
        
        # 출근 기록이 목표 출근시간보다 이르거나 주말이면 True
        return all(time_calculator(val)<=x or (startday+idx)%7 in [6,0] for idx, val in enumerate(lst))
    
    cnt = 0
    for i in range(len(schedules)):
        present = all_smaller(timelogs[i], schedules[i])
        if present:
            cnt+=1
    
    return cnt