def solution(prices):
    answer = []
    prices_len = len(prices)
    
    for i in range(prices_len):
        duration = 0
        for j in range(i+1, prices_len):
            duration +=1
            if prices[i] > prices[j]:
                break
        answer.append(duration)
    return answer