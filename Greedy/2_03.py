#숫자 카드 게임 greedy

from sys import stdin
from time import time

#내가 푼 방법

# start = time()
# N, M = map(int, stdin.readline().split())

# list = [list(map(int, stdin.readline().split())) for n in range(N)]

# for n in list:
#     n.sort()
# small_list = []
# for small in list:
#     small_list.append(small[0])


# print(max(small_list))
# end = time()

# print(int(end - start))

start = time()

N, M = map(int, stdin.readline().split())

result = 0

for _ in range(N):
    data = list(map(int, stdin.readline().split()))

    min_value = min(data)

    result = max(result, min_value)

print(result)

end = time()

print(int(end - start))











# 3 3
# 3 1 2
# 4 1 4
# 2 2 2


# 2 4
# 7 3 1 8
# 3 3 3 4