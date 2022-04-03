#서로소 집합(Disjoint Sets)
#   서로소 집합의 자료구조란 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
#   서로소 집합 자료구조는 union과 find 이2개이 연산으로 조작 union-find자료구조라고 불리기도 함
#   1.union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인
#       A와 B의 루트 노드 A', B'를 각각 찾는다
#       A'를 B'의 부모 노드로 설정한다(B'가 A'를 가리키도록 한다)
#   2.모든 union(합집합) 연산을 처리할 때까지 1번과정을 반복

#기본적인 서로소 집합 알고리즘 소스코드

#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):

    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
    #     return find_parent(parent, parent[x])

    # return x
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

for i in range(e):
    a, b  = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가  속한 집합 : ', end = '')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블 : ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')


# 6 4
# 1 4
# 2 3
# 2 4
# 5 6