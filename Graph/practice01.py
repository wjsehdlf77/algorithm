#팀 결성

#0은 팀 합치기, 1은 같은 팀 여부 확인

from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

team = [0] * (n + 1)

for i in range(n + 1):
    team[i] = i

def find_team(team, student):
    if team[student] != student:
        team[student] = find_team(team, team[student])
    return team[student]


def union_team(team, student1, student2):
    student1 = find_team(team, student1)
    student2 = find_team(team, student2)

    if student1 > student2:
        team[student1] = student2
    else:
        team[student2] = student1

for _ in range(m):
    calc, student1, student2 = map(int, input().split())

    if calc == 0:
        union_team(team, student1, student2)
    else:
        if find_team(team, student1) == find_team(team, student2):
            print('YES')
        else:
            print('NO')


# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1
