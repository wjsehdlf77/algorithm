#개미전사

from sys import stdin

N = int(stdin.readline())

K = list(map(int, stdin.readline().split()))

d = [0] * 100

d[0] = K[0]
d[1] = max(K[0], K[1])  #인데스 1과 2를 메모이제이션 해놓고 그 다음 bottom-up

for i in range(2, N):
    
    d[i] = max(d[i - 1], d[i - 2] + K[i] )

print(d[N-1])





     


# 4
# 1 3 1 5