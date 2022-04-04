#도시 분할 계획

from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

villege = [0]* (n + 1)

for i in range(1, n + 1):
    villege[i] = i

def find_villege(villege, house):
    if villege[house] != house:
        villege[house] = find_villege(villege, villege[house])
    return villege[house]

def union_house(villege, house1, house2):
    house1 = find_villege(villege, house1)
    house2 = find_villege(villege, house2)

    if house1 > house2:
        villege[house1] = house2
    else:
        villege[house2] = house1


result = []
edges = []

for _ in range(m):
    house1, house2, cost = map(int, input().split())

    edges.append((cost, house1, house2))

edges.sort()

for edge in edges:
    cost, house1, house2 = edge

    if find_villege(villege, house1) != find_villege(villege, house2):
        union_house(villege, house1, house2)
        result.append(cost)

result.remove(max(result))

print(sum(result))











# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4