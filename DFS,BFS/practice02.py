#미로 탈출
from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

data = []

for _ in range(N):
    data.append(list(map(int, stdin.readline().rstrip())))

# num = 0

# def bfs(x, y, data):
#     q = deque([(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)])

#     while q:
#         nx, ny = q.popleft()
#         if nx <= -1 or ny <= -1 or nx >= N or ny >= M:
#             return 0
#         if data[nx][ny] == 1:
#             num += 1
#             data[nx][ny] = num
#             q.append((nx - 1, ny))
#             q.append((nx + 1, ny))
#             q.append((nx, ny - 1))
#             q.append((nx, ny + 1))
#     return data
# print(bfs(0, 0, data))
#상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            if data[nx][ny] == 0:
                continue

            if data[nx][ny] == 1:
                data[nx][ny] = data[x][y] + 1;
                queue.append((nx, ny))

    return data[N - 1][M - 1]

    


print(bfs(0, 0))


        






        
        
        












# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111