def solution(word):
    weight = [781, 156, 31, 6, 1]
    order = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}

    answer = 0
    for i in range(len(word)):
        answer += order[word[i]] * weight[i] + 1

    return answer