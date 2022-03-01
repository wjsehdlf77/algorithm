#음료수 얼려먹기

from sys import stdin

N, M = map(int, stdin.readline().split())
data = []
for _ in range(N):
    a = [int(n) for n in str(stdin.readline().rstrip())]
    data.append(a)

def dfs(x, y):
    if y <= -1 or x <= -1 or x >= N or y >= M:
        return False
    
    if data[x][y] == 0:
        data[x][y] = 1

        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1
print(result)


    
    





    
    
    
    








# 15 14 
# 00000111100000 
# 11111101111110 
# 11011101101110 
# 110111011000000 
# 11011111111111
# 11011111111100
# 11000000011111 
# 01111111111111 
# 00000000011111 
# 01111111111000 
# 00011111111000 
# 00000001111000 
# 11111111110011 
# 11100011111111 
# 11100011111111