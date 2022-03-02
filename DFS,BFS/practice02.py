#미로 탈출
from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

data = []

for _ in range(N):
    data.append(list(map(int, stdin.readline().rstrip())))

num = 0

def bfs(x, y, data):
    q = deque([(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)])

    while q:
        nx, ny = q.popleft()
        if nx <= -1 or ny <= -1 or nx >= N or ny >= M:
            return 0
        if data[nx][ny] == 1:
            num += 1
            data[nx][ny] = num
            q.append((nx - 1, ny))
            q.append((nx + 1, ny))
            q.append((nx, ny - 1))
            q.append((nx, ny + 1))
    return data
print(bfs(0, 0, data))



        






        
        
        












# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111