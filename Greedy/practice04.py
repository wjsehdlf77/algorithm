#1이 될 때까지 greedy

from sys import stdin
from time import time

#내가푼 방법

# N, K = map(int, stdin.readline().split())
# start = time()

# count = 0

# while N > 1:
#     if N % K == 0:
#         N //= K
#         count += 1

#     else:
#         N -= 1
#         count += 1

# print(count)

# end = time()

# print(end - start)

#답안지개조



N, K = map(int, stdin.readline().split())

count = 0

while True:
    target = (N // K) * K
    
    count += (N - target)
    N = target
 
    if N < K:
        break
    N //= K
    count += 1

count += (N - 1)
print(count)
