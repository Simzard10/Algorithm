from collections import deque

n = int(input())

example = []

result_stack = deque()

result = []

for i in range(n):
    example.append(int(input()))

flag = True

temp = 1
for i in example:
    for j in range(temp, i+1):
        result_stack.append(j)
        result.append('+')
        temp = j+1

    if result_stack[len(result_stack)-1] == i:
        result_stack.pop()
        result.append('-')
    else: 
        break

if len(result_stack) == 0:     
    for i in result:
        print(i)
else: 
    print("NO")