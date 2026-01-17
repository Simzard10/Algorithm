N, X = map(int, input().split())
statistics = list(map(int, input().split()))

current_sum = 0
for i in range(X):
    current_sum += statistics[i]

max_sum = current_sum
count = 1

for i in range(X, N):
    current_sum += statistics[i]
    current_sum -= statistics[i - X]

    if current_sum > max_sum:
        max_sum = current_sum
        count = 1
    elif current_sum == max_sum:
        count += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)