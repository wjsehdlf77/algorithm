#그리디 큰수의 법칙 greedy

from sys import stdin
from time import time

#내가 푼 부분

# start = time()
# N, M, K = map(int, stdin.readline().split())

# list = [int(n) for n in stdin.readline().split()]

# list.sort(reverse=True)

# total = 0

# while M > 0:
#     total += (list[0] * K)
#     M -= K
#     total += list[1]
#     M -= 1

# print(total)

# end = time()

# print(end - start)

start = time()
    
N, M, K = map(int, stdin.readline().split())

data = list(map(int, stdin.readline().split()))

data.sort()

first = data[N - 1]
second = data[N - 2] 

result = 0
first_result = 0
second_result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        first_result += first
        M -= 1
    if M == 0:
        break
    result += second
    second_result += second
    M -= 1

print(result)
print(first_result)
print(second_result)

end = time()

print(end - start)







# 5 8 3
# 2 4 5 4 6