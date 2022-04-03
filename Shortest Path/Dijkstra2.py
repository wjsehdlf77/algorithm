#개선된 다익스트라 알고리즘
#   힙 자료구조는 우선순위 큐를 구현하기 위하여 사용하는 자료구조 중 하나
#   우선순위 큐를 구현할 때는 최소 힙 혹은 최대 힙을 이용
#   파이썬 라이브러리에서는 기본적으로 최소 힙 구조를 이용하는데 다익스트라 최단 경로 알고리즘에는 적은 노드를 우선하여 방문하므로 적합
#   최소 힙을 최대 힙처럼 사용하기 위해서 우선순위에 해당하는 값을 음수로 바꾸고 큐에서 꺼낸 다음 다시 -를 붙여서 원래값으로 돌리는 기법을 많이 사용
#   PriorityQueue보다 heapq가 조금 더 빠르다
#   앞 코드와 비교했을 때 get_samllest_node()라는 함수를 작성할 필요가 없다는 특징
#   최단 거리가 가장 짧은 노드 를 선택하는 과정를 다익스트라 최단경로함수 안에서 우서운위 큐를 이용하는 방식으로 대체

from sys import stdin
import heapq

input = stdin.readline

INF = int(1e9)      #무한을 의하는 값을 10억으로 설정

#노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())

#시작 노드
start = int(input())

#각 노드의 연결된 정보
graph = [[] for _ in range(n + 1)]

#최단 고리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

#간선의 모든 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(start)


for i in range(1, n + 1):

    if distance[i] == INF:
        print('infinity')
    else:
        print(distance[i])




# 6 11
# 1 
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2