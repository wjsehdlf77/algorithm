#성적이 낮은 순서로 학생 출력하기

from sys import stdin

N = int(stdin.readline())

data = []

for _ in range(N):
    data.append(list(stdin.readline().split()))


data = sorted(data, key = lambda student : int(student[1]))

for student in data:
    print(student[0], end=' ')

# 2
# 홍길동 95
# 이순신 77

