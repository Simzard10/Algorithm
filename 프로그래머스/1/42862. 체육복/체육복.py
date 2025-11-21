def solution(n, lost, reserve):
    answer = 0
    
    for i in range(1, n+1):
        if (i in lost and i in reserve):
            reserve.remove(i)
            lost.remove(i)

    for i in range(1, n+1): 
        if (i in lost): 
            if (i-1 > 0 and i-1 in reserve):
                reserve.remove(i-1)
                lost.remove(i)
                answer+=1
            elif (i+1 < n+1 and i+1 in reserve):
                reserve.remove(i+1)
                lost.remove(i)
                answer+=1
        else:
            answer +=1
    return answer