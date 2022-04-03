#미래도시

#n = 회사수(노드) m = 경로개수(간선= 1)
#x = 방문판매회사 k = 소개팅회사
# 1 -> k -> x 가장 빠른 길


#내가 푼 다익스트라 방법
# import heapq
# from sys import stdin

# input = stdin.readline

# INF = int(1e9)

# n, m = map(int, input().split())

# graph = [[] for _ in range(n + 1)]

# distance = [INF] * (n + 1)

# for _ in range(m):
#     route1, route2 = map(int, input().split())
#     if route2 not in graph[route1]: 
#         graph[route1].append(route2)
#     if route1 not in graph[route2]: 
#         graph[route2].append(route1)


# x, k = map(int, input().split())


# def company_route(start = 1):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
    
#     while q:
#         dist, now = heapq.heappop(q)
#         if dist > distance[now]:
#             continue

#         for i in graph[now]:
#             cost = dist + 1

#             if cost < distance[i]:
#                 distance[i] = cost
#                 heapq.heappush(q, (cost, i))


# company_route()
# first = distance[k]
# company_route(k)
# end = distance[x]

# if  (first + end) < INF:
#     print(first + end)
# else:
#     print(-1) 

#플로이드 워셜 방법

from sys import stdin

input = stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF]*(n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())


for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


if(graph[1][k] + graph[k][x]) < INF:
    print(graph[1][k] + graph[k][x])
else:
    print(-1)




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
