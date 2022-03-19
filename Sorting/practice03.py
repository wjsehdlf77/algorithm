#두 배열의 원소 교체

from sys import stdin

N, K = map(int, stdin.readline().split())
A = [int(n) for n in stdin.readline().split()]
B = [int(n) for n in stdin.readline().split()]

A = sorted(A)
B = sorted(B, reverse=True)

for i in range(K):
    if A[i] >= B[i]: continue

    A[i], B[i] = B[i], A[i]

print(sum(A))
