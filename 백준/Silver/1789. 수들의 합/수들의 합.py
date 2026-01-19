S = int(input())

current_sum = 0
number = 1

while current_sum + number <= S:
    current_sum += number
    number += 1

print(number - 1)