def solution(arr):
    answer = []
    arr.reverse()
    while arr:
        temp = arr.pop()
        if len(answer) == 0:
            answer.append(temp)
        else:   
            latest = answer[len(answer)-1]
            if temp != latest:
                answer.append(temp)
            else:
                continue
            
    return answer