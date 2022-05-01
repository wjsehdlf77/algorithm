#greedy 만들 수 없는 금액

from sys import stdin

N = int(stdin.readline())

data = list(map(int, stdin.readline().split()))

data.sort()

target = 1

for i in data:
    if i <= target:
        target  += i

print(target)




# 5
# 3 2 1 1 9
