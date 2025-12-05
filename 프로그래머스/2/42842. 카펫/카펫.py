def solution(brown, yellow):
    answer = []
    # yellow의 약수를 구함
    yellow_yaksu = []
    for i in range(1, yellow+1):
        if (yellow%i==0):
            yellow_yaksu.append(i)
    
    
    for i in yellow_yaksu:
        for j in yellow_yaksu:
            if (i<j):
                continue
            if (i>=j and i*j == yellow and ((i+2))*(j+2)==(yellow+brown)):
                answer.append(i+2)
                answer.append(j+2)
                return answer
    
    return answer