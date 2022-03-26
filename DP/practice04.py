#효율적인 화폐 구성

from sys import stdin


# 내방법
N, M = map(int, stdin.readline().split())

d = [10001] * (M + 1)
d[0] = 0

data = []

for _ in range(N):
    data.append(int(stdin.readline()))

for i in data:
    for j in range(0, M + 1):
        if d[j] > 0:
            d[j] = min(d[j], d[j - i] + 1)
            print(d[i - i] + 1, end = ', ')
            

if d[M] == 10001:
    print(-1)
else:
    print(d[15])










# 1 15
# 2

# 2 15
# 2
# 3

# 3 4
# 3
# 5
# 7

