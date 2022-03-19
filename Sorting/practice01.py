#위에서 아래로

from sys import stdin

N = int(stdin.readline())

data = []

for _ in range(N):
    
    data.append(int(stdin.readline()))

data = sorted(data, reverse=True)

for i in data:
    print(i, end=' ')

# 3
# 15
# 27
# 12