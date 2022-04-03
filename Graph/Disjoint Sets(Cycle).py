#서로소 집합을 활용한 사이클 판별

#   1.각 간선을 확인하며 두 노드의 루트 노드를 확인
#       루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행
#       루트 노드가 서로 같다면 사이클(Cycle)이 발생
#   2.그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다.

#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):

    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
    #개선된 경로 압축 기법
        parent[x] = find_parent(parent, parent[x])
    return parent[x] 

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0]* (v + 1)

for i in range(1, v + 1):
    parent[i] = i

cycle = False #사이클 발생 여부

for i in range(e):
    a, b  = map(int, input().split())
    #사이클이 발생한 경우
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클이 발생했습니다')
else:
    print('사이클이 발생하지 않았습니다')

# 3 3
# 1 2
# 1 3
# 2 3
