# 11048

from sys import stdin

#bottom-up

def route(N, M):
    
    

N, M = map(int, stdin.readline().split())

column = [list(map(int, stdin.readline().split())) for _ in range(N)]

print(column)