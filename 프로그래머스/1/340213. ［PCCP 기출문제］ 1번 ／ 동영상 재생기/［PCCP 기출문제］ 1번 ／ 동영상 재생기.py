def timesec(time):
    m, s = map(int, time.split(':'))
    return m*60 + s

def op_remove(pos, op_start, op_end):
    if op_start <= pos and pos <= op_end:
        pos = op_end
    return pos

def solution(video_len, pos, op_start, op_end, commands):
    video_len, pos, op_start, op_end = map(timesec, [video_len, pos, op_start, op_end])
    pos = op_remove(pos, op_start, op_end)
        
    for com in commands:
        if com == 'next':
            pos = pos+10 if (video_len - pos) >= 10 else video_len
            pos = op_remove(pos, op_start, op_end)
        else: # prev
            pos = pos-10 if pos >= 10 else 0
            pos = op_remove(pos, op_start, op_end)
            
    return f"{pos//60:02}:{pos%60:02}"