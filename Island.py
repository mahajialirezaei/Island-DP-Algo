def print_table(dp, k):
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            print(dp[i][j][k], end=" ")
        print()
    print("\n")

def probability_death(x: int, y: int, m: int, n: int):
    dp = []
    ls = [0, n - 1]
    for i in range(n):
        dp.append([])
        for j in range(n):
            dp[i].append([])
            for k in range(m + 1):
                dp[i][j].append(0)
    for k in range(1, m + 1):
        for i in range(n):
            for j in range(n):
                if i in ls or j in ls:
                    dp[i][j][1] = 0.25
                if i in ls and j in ls:
                    dp[i][j][1] = 0.5
                dp[i][j][0] = 0
                count = 0
                if i < n - 1:
                    dp[i][j][k] += dp[i + 1][j][k - 1]
                    count += 1

                if j < n - 1:
                    dp[i][j][k] += dp[i][j + 1][k - 1]
                    count += 1

                if i > 0:
                    dp[i][j][k] += dp[i - 1][j][k - 1]
                    count += 1

                if j > 0:
                    dp[i][j][k] += dp[i][j - 1][k - 1]
                    count += 1


                if count > 0 and i not in ls and j not in ls:
                    dp[i][j][k] /= count
            dp[i][j][0] = 0

    for k in range(m + 1):
        print_table(dp, k)

    return dp[x][y][m]

n = 5
x = 1
y = 1
m = 3
print(probability_death(x, y, m, n))
# print(probability_death(1, 1, 2, 3))




