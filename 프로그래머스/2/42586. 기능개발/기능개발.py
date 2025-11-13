def solution(progresses, speeds):
    i = 0 
    progress = []
    answer = []
    for temp in progresses:
        progress_time = int(((99 - temp)/(speeds[i]))+1)
        progress.append(progress_time)
        i+=1
    progress.reverse()
    answer_stack = []
    
    while progress: # 비어 있을 때 까지 진행
    
        temp = progress.pop()
        if not answer:
            answer.append(1)
            answer_stack.append(temp)
        elif answer_stack[-1] >= temp: # 먼저 배포되어야하는 작업이 더 늦게 끝날때 
            answer[-1] += 1
        else: # 먼저 배포되어야하는 작업이 더 빨리 끝날 때 
            answer.append(1)
            answer_stack.append(temp)
    
    return answer