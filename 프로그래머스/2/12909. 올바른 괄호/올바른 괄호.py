def solution(s):
    answer = True
    temp = []
    for i in s:
        if i == "(":
            temp.append("(")
        else:
            temp.append("(")
            if temp[len(temp)-1] == "(" and len(temp) > 1:
                temp.pop()
                temp.pop()
            else:
                answer = False
    
    if len(temp) > 0:
        return False
    return True