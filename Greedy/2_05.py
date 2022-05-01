#볼링공 고르기 1차복습

from sys import stdin

n, m = map(int, stdin.readline().split())

value = [int(n) for n in stdin.readline().split()]

count = 0

while value:

    weight = value.pop()
    for i in value:
        if weight != i:
            count += 1

print(count)


# 5 3
# 1 3 2 3 2

# 8 5
# 1 5 4 3 2 4 5 2
