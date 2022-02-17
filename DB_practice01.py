# 11048

from sys import stdin

def route(N, M):
    if N == -1 or M == -1:
        return 0 
    return max(column[N][M] + route(N - 1, M), column[N][M] + route(N , M - 1), column[N][M] + route(N - 1 , M - 1))

N, M = map(int, stdin.readline().split())

column = [list(map(int, input().split())) for _ in range(N)]

print(route(N - 1,M - 1))