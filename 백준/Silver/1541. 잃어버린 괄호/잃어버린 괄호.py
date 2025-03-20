

# 55-(50+40)

# 55-(50+40)-40

# 55+40-50

# 55-50-40

# 55-50+40-40

# 그리디


exp = list(map(str, input()))
answer_exp = []

numbers = []
operators = []

num = "" # 현재 숫자 저장 변수
for char in exp: # 식을 반복문 돌면서 식 완성
    if char.isdigit(): # 숫자인 경우
        num += char
    else: # 연산자인 경우
        numbers.append(int(num))
        operators.append(char)
        num = ""
numbers.append(int(num)) # 마지막 숫자

answer = numbers[0]
is_minus = False # - 등장 여부 체크

for i in range(1, len(numbers)): 
    if operators[i-1] == "-":
        is_minus = True  # `-` 이후 숫자들은 모두 빼기
        
    if is_minus:  
        answer -= numbers[i]  # `-` 이후 숫자들은 모두 빼기
    else:
        answer += numbers[i]  # `+`면 더하기

# - 가 나오면 괄호시작, 다음 -가 나오면 괄호 닫기, 안나오고 끝나면 괄호 닫기

print(answer)

        


# 식에서 숫자는 숫자 끼리 묶어서, 
