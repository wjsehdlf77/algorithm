#개미전사

from sys import stdin

N = int(stdin.readline())

K = list(map(int, stdin.readline().split()))

d = [0] * 100

for i in range(1, N + 1):
    d[i] = K[i-1]
    
    d[i] = max(d[i], d[i-1])

print(d)





     


# 4
# 1 3 1 5