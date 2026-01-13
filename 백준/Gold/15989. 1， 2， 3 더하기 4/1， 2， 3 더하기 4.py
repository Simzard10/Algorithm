T = int(input())

result = []

dp = []
dp = [1] * 100001

for i in range(2, 100001):
    dp[i] += dp[i-2]

for i in range(3, 100001):
    dp[i] += dp[i-3]

for _ in range(T):
    n = int(input())
    result.append(dp[n])

for i in result:
    print(i)