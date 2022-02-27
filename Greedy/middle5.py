#greedy 볼링공 고르기

from sys import stdin
9
N, M = map(int,stdin.readline().split())

K = list(map(int, stdin.readline().split()))

total = (len(K) * (len(K) - 1)) // 2
print(total)
count = 0

K_SET = list(set(K))

for data in K_SET:
    num = K.count(data)
    if num > 1:
        count += num
        total -= (count * (count-1)) // 2
        
        count = 0
print(total)


# 5 3
# 1 3 2 3 2