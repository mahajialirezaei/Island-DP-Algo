def probability_death(x:int, y:int, m:int, n:int):
    dp = []
    ls = [0, n-1]
    for i in range(n+1):
        dp.append([])
        for j in range(n+1):
            dp[i].append([])
            for k in range(m+1):
                dp[i][j].append(0)

    for i in range(n):
        for j in range(n):
            for k in range(m+1):
                if (i in ls and j in ls):
                    dp[i][j][1] = 0.25
                if (i in ls and i == j):
                    dp[i][j][1] = 0.5
                if k == 0:
                    dp[i][j][k] = 0
                dp[i][j][k] = (dp[i-1][j][k-1] + dp[i][j-1][k -1] + dp[i+1][j][k-1] + dp[i][j+1][k-1]) / 4
                print(dp[i][j][k], i, j, k)
    return dp[x][y][m]



n = 5
x = 1
y= 1
m = 3
print(probability_death(x, y, m, n))



