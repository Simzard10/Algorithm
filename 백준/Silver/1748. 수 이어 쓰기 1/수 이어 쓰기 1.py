N = int(input())

A = len(str(N)) # N의 자릿수

answer = 0

answer += (N - (10**(A-1)) +1) * A  

for i in range(A-1, 0, -1): # 자릿수부터 하나씩 감소하면서 시작
    answer += 9*(10**(i-1)) * i

print(answer)
