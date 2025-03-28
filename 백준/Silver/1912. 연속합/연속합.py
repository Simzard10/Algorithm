n = int(input())
dp = [0]* n

num_arr = list(map(int, input().split()))

dp[0] = num_arr[0]
# dp[1] = max(dp[0] + num_arr[1], num_arr[1])
# dp[2] = max(dp[1] + num_arr[2], num_arr[2])
for i in range(1, n):
    dp[i] = max(dp[i-1] + num_arr[i], num_arr[i])

print(max(dp))