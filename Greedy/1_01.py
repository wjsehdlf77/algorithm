#모험가길드

from sys import stdin

#내가만든 방법

# N = int(stdin.readline())


# adventurers = list(map(int, stdin. readline().split()))

# adventurers.sort(reverse=True)

# group = 0

# for i in range(len(adventurers)):
#     if len(adventurers) == 0:
#         break
#     a = adventurers.pop(0)
#     group += 1
#     for _ in range(a - 1):
#         if len(adventurers) == 0:
#             break
#         adventurers.pop(0)

# print(group)

        


# N = int(stdin.readline())

# adventurers = list(map(int, stdin. readline().split()))

# adventurers.sort()

# group = 0

# count = 0

# for i in adventurers:
#     count += 1
#     if count >= i:
#         group += 1
#         count = 0
# print(group)


# 5
# 2 3 1 2 2

# 7
# 1 1 2 2 2 2 3 3


N = int(stdin.readline())

data = list(map(int, stdin.readline().split()))

data.sort()

group = 0

count = 0

for d in data:
    group += 1

    if group == d:
        count += 1
        group = 0

print(count)

