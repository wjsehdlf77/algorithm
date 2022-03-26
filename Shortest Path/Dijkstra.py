#다익스트라 최단 경로 알고리즘(Dijkstra)
#   그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
#   음의 간선이 없을 때 정상적으로 동작 (음의 간선이란 0보다 작은 값을 가지는 간선)

        # 1. 출발 노드를 설정
        # 2. 최단 거리 테이블을 초기화
        # 3. 방문하지 않은 노드 중에서 최단 거리가 짧은 노드르 선택
        # 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
        # 5. 위 과정 3, 4반복

#   다익스트라 최단 거리 알고리즘이 진행되면서 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해

#간단한 다익스트라 알고리즘
#   시간복잡도 O(V^2)
#   단계마다 '방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택'하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차 탐색)
#   시간복잡도 O(V^2)이므로 전체 V(노드)의 개수가 5000개 이하라면 이 코드로 풀 수 있지만 V가 10000이 넘어가면 문제 해결이 어렵다

from sys import stdin

input = stdin.readline

INF = int(1e9)      #무한을 의하는 값을 10억으로 설정

#노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())

#시작 노드
start = int(input())

#각 노드의 연결된 정보
graph = [[] for _ in range(n + 1)]

#방문 체크
visited = [False] * (n + 1)

#최단 고리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

#간선의 모든 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())

    graph[a].append((b, c))

#방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환

def get_smallest_node():
    min_value = INF
    index = 0       #최단 거리가 가장 짧은 노드의 번호
    for i in range(1, n + 1):
        if distance[i] < min_value and (not visited[i]):      #min_value가 갱신되면서 갱신된 min_value값 보다 크면 조건문을 통과못해서 결국 최소값의 인덱스를 얻는다
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    #시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    #시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for _ in range(n - 1):

        #현재 최단 거리가 가장 짧은 노드를꺼내서, 방문 초리
        now = get_smallest_node()

        visited[now] = True

        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            
            #현재 노드를 거챠서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


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

