#커리큘럼

from collections import deque
from sys import stdin

n = int(stdin.readline())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
num_time = [0] * (n + 1)



for i in range(1, n + 1):
    data = list(map(int, stdin.readline().split()))

    num_time[i] = data[0]
    for x in data[1 : -1]:    
        graph[i].append(x)
        indegree[x] += 1      

def topology(a= 0):

    max_time = 0
    q = deque()

    for i in indegree:
        if i == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            max_time = max(num_time[i], max_time)
            if indegree[i] == 0:
                q.append(i)
        a += max_time
        max_time = 0

time = 0

topology(time)

print(time)





# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1