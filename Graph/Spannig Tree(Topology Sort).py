#위상 정렬(Topology Sort)
#   순서가 정해져 있는 일련의 작업을 차례대로 수행. 좀더 이론적으로 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
#   진인 차수(Indegree)란 특정한 노드로 '들어오는' 간선의 개수
#       1.진입차수가 0인 노드를 큐에 넣는다.
#       2.큐가 빌 때까지 다음의 과정을 번복한다.
#           큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
#           새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
#   시간 복잡도는 O(V + E)

#위상 정려 소스코드
from collections import deque


#노드의 개수와 간선의 개수를 입력
v, e = map(int, input().split())

#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)

#각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(v + 1)]

#방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

    #진입차수를 1증가
    indegree[b] += 1

#위상 정렬 함수
def topology_sort():
    result = []     #알고리즘 수행 결과를 담을 리스트
    q = deque()     #큐 기능을 위한 deque 라이브러리 사용

    #처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()

# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4

