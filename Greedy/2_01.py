#거스름돈 greedy

# 500원 100원 50원 10원 최소한으로 거스름돈을 줘라

from sys import stdin

#내가 푼 부분

# N = int(stdin.readline())

# count = 0
# while N >= 500:
#     N -= 500
#     count += 1
#     print(N)

# while N >= 100:
#     N -= 100
#     count += 1

# while N >= 50:
#     N -= 50
#     count += 1

# while N >= 10:
#     N -= 10
#     count += 1

# print(count)

#책 정답

N = int(stdin.readline())

coins = [500, 100, 50, 10]

count = 0

for coin in coins:
    count += (N//coin)
    N %= coin

print(count)




