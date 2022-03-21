#바닥 공사

from sys import stdin

N = int(stdin.readline())

d = [0] * 10

d[1] = 1
d[2] = 3

for i in range(3, N + 1): 

    d[i] = (d[i - 1] + d[i - 2] * 2) % 796796
    print(d)

print(d[N])