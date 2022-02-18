# 11048

from sys import stdin

#bottom-up

def route(N, M):
    candy = 0
    for m in range(M):
        candy += max(column[m + 1][m], column[m][m + 1], column[m + 1][m + 1])

    return candy
        
N, M = map(int, stdin.readline().split())
column = [list(map(int, stdin.readline().split())) for _ in range(N)]
print(route(N, M))