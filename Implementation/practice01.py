# #구현문제 상하좌우

# from sys import stdin


# N = int(stdin.readline())

# routes = list(stdin.readline().split())
# x, y = 1, 1
# # L, R, U, D
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# for route in routes:
#     for i in range(len(move_types)):
#         if route == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or ny < 1 or nx > N or ny > N:
#         continue
#     x, y = nx, ny

# print(x, y)


    






# 5
# R R R U D D

from sys import stdin

N = int(stdin.readline())

dataes = list(stdin.readline().split())

# L R U D

dx = [0, 0, -1, 1]
dy = [-1, 1, 0 ,0]
routes = ["L", "R", "U", "D"]

x, y = 1, 1

for data in dataes:
    index = routes.index(data)
    if data == routes[index]:
        nx = dx[index] + x
        ny = dy[index] + y
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x = nx
    y = ny


print(x, y)




