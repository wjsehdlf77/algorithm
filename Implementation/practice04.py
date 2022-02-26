#구현문제 게임 개발

from sys import stdin

N, M = map(int, stdin.readline().split())

A, B, d = map(int, stdin.readline().split())

map = [list(map(int,stdin.readline().split())) for _ in range(N)]
            #북 동 남 서
compass = [0, 1, 2, 3]
steps = [(0, -1), (-1, 0), (0, 1), (1, 0)]
count  = 1
map[A][B] = 1
while True:
    if map[A-1][B] == 1 and map[A][B-1] == 1 and map[A+1][B] == 1 and map[A][B + 1] == 1:
        break
    a, b = steps[d]
    nA = A + a
    nB = B + b

    if d == 0:
        d = 3
    else:
        d -= 1

    if map[nA][nB] == 1:
        continue
    A = nA
    B = nB
    map[A][B] = 1
    count += 1

       
print(count)


        
        



    
    

    






# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 0 0 1
# 1 1 1 1

