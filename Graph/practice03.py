#커리큘럼

from collections import deque
from sys import stdin
import copy

n = int(stdin.readline())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
num_time = [0] * (n + 1)



for i in range(1, n + 1):
    data = list(map(int, stdin.readline().split()))

    num_time[i] = data[0]

    for x in data[1 : -1]:    
        graph[x].append(i)
        indegree[i] += 1      

def topology_sort():

    result = copy.deepcopy(num_time)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:

        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + num_time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])

topology_sort()







# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1