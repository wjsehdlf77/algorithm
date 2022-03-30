#미래도시

#n = 회사수(노드) m = 경로개수(간선= 1)
#x = 방문판매회사 k = 소개팅회사
# 1 -> k -> x 가장 빠른 길

from sys import stdin

input = stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    route1, route2 = map(int, input().split())
    if route2 not in graph[route1]: 
        graph[route1].append(route2)
    if route1 not in graph[route2]: 
        graph[route2].append(route1)


end, first = map(int, input().split())

def K(start = 1):
    q = []
    







# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5


# 4 2
# 1 3
# 2 4
# 3 4
