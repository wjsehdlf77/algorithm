#효율적인 화폐 구성

from sys import stdin


# 내방법
# N, M = map(int, stdin.readline().split())

# d = [10001] * (M + 1)
# d[0] = 0

# data = []

# for _ in range(N):
#     data.append(int(stdin.readline()))

# for i in data:
#     for j in range(0, M + 1):
#         if d[j] > 0:
#             d[j] = min(d[j], d[j - i] + 1)
#             print(d[i - i] + 1, end = ', ')
            

# if d[M] == 10001:
#     print(-1)
# else:
#     print(d[15])


N, M = map(int, stdin.readline().split())

d = [10001] * (M + 1)
d[0] = 0

data = []

for _ in range(N):
    data.append(int(stdin.readline()))

for i in range(N):
    for j in range(data[i], M + 1):         #데이터의 순서에 따라 그 값에 맞게 루프문이 시작한다
        if d[j - data[i]] != 10001:
            d[j] = min(d[j], d[j - data[i]] + 1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])












# 1 15
# 2

# 2 15
# 2
# 3

# 3 4
# 3
# 5
# 7

