#구현문제 게임 개발

from sys import stdin

#내방식

# N, M = map(int, stdin.readline().split())

# A, B, d = map(int, stdin.readline().split())

# map = [list(map(int,stdin.readline().split())) for _ in range(N)]
#             #북 동 남 서
# compass = [0, 1, 2, 3]
# steps = [(0, -1), (-1, 0), (0, 1), (1, 0)]
# count  = 1
# map[A][B] = 1
# while True:
#     if map[A-1][B] == 1 and map[A][B-1] == 1 and map[A+1][B] == 1 and map[A][B + 1] == 1:
#         break
#     a, b = steps[d]
#     nA = A + a
#     nB = B + b

#     if d == 0:
#         d = 3
#     else:
#         d -= 1

#     if map[nA][nB] == 1:
#         continue
#     A = nA
#     B = nB
#     map[A][B] = 1
#     count += 1

# print(count)


#답안방식

N, M = map(int, stdin.readline().split())

A, B, dirc = map(int, stdin.readline().split())

map = [list(map(int,stdin.readline().split())) for _ in range(N)]
d = [[0] * M for _ in range(N)]

map[A][B] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global dirc
    dirc -= 1
    if dirc == -1:
        dirc= 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = A + dx[dirc]
    ny = B + dy[dirc]
    if d[nx][ny] == 0 and map[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[dirc]
        ny = y - dy[dirc]

        if map[nx][ny] == 0:
            x = nx
            y = ny

        else:
            break
        turn_time = 0

print(count)


        
        



    
    

    






# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 0 0 1
# 1 1 1 1

