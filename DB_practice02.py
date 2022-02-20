# 11048

from sys import stdin

#bottom-up

def route(N, M):

    dp = [[0] * (M + 1)] * (N + 1)
    for n in range(1, N + 1):
        for m in range(1, M + 1):
            dp[n][m] = max(dp[n -1][m], dp[n][m - 1], dp[n - 1][m - 1]) + column[n-1][m-1]
    return dp[N][M]
    
N, M = map(int, stdin.readline().split())

column = [list(map(int, stdin.readline().split())) for _ in range(N)]

print(route(N, M))



