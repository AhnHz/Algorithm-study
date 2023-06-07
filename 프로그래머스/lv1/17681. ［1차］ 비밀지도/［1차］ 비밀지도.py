def solution(n, arr1, arr2):
    answer = []
  
    for i in range(n):
        answer.append(str(bin(arr1[i] | arr2[i]))[2:].zfill(n))
        
        answer[i] = answer[i].replace('1', '#').replace('0', ' ')
        #answer[i] = answer[i].replace('0', ' ')
        
    return answer