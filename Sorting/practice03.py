#두 배열의 원소 교체


# 내 방법
# from sys import stdin

# N, K = map(int, stdin.readline().split())
# A = [int(n) for n in stdin.readline().split()]
# B = [int(n) for n in stdin.readline().split()]

# A = sorted(A)
# B = sorted(B, reverse=True)

# for i in range(K):
#     if A[i] >= B[i]: continue

#     A[i], B[i] = B[i], A[i]

# print(sum(A))

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))


# 5 3
# 1 2 5 4 3
# 5 5 6 6 5
