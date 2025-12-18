def solution(m, n, puddles):
    MOD = 1_000_000_007

    dp = [[0] * m for _ in range(n)]
    
    print(dp)

    for x, y in puddles:
        dp[y-1][x-1] = -1

    dp[0][0] = 1

    for j in range(1, m):
        if dp[0][j] == -1:
            dp[0][j] = 0
        else:
            dp[0][j] = dp[0][j-1]

    for i in range(1, n):
        if dp[i][0] == -1:
            dp[i][0] = 0
        else:
            dp[i][0] = dp[i-1][0]

    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] == -1:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) 

    return dp[n-1][m-1] % MOD