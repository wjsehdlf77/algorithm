#신장 트리(Spannig Tree)
#   하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미
#   신장 트리 알고리즘 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘을 '최소 신장 트리 알고리즘' 이다
#   대표적인 최소 신상트리 알고리즘 크루스칼 알고리즘(Kruskal Algorithm)이 있다.

#   크루스칼 알고리즘(Kruskal Algorithm)
#       가장 적은 비용으로 모든 노드를 연결할 수 있는데 그리디 알고리즘으로 분류
#           1.간선 데이터를 비용에 따라 오름차순으로 정렬
#           2.간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
#               사이클을 발생하지 않는 경우 최소 신장 트리에 포함
#               사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
#           3.모든 간선에 대하여 2번의 과정을 반복한다.
#       시간복잡도는 간선의 개수가 E개일 때 O(ElogE)의 시간복잡도를 가진다(간선을 정렬하는 부분이 제일 시간을 많이 차지한다)

#크루스칼 알고리즘 소스코드

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

v, e = map(int, input().split())
parent = [0] * (v + 1)

#모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

#모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())

    #비용순으로 정렬하기 위하여 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

#간선을 비용순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge

    #사이클이 발생하지 않을 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25
