#전보

import heapq
from sys import stdin

input = stdin.readline

n ,m, c = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())

    graph[x].append((y, z))

time = [INF] * (n + 1)


def message(start):
    q = []
    heapq.heappush(q, (0, start))
    time[start] = 0

    while q:
        t, now = heapq.heappop(q)

        if time[now] < t:
            continue
        for city, tm in graph[now]:
            cost = t + tm

            if cost < time[city]:
                time[city] = cost
                heapq.heappush(q, (cost, city))


message(c)

city_num = len([n for n in time if n >=1 and n < INF])

time_max = max([n for n in time if n != INF])

print(f'{city_num} {time_max}')





# 3 2 1
# 1 2 4
# 1 3 2






