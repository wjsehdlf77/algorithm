#1로 만들기

from sys import stdin

dp = [0] * 11

X = int(stdin.readline())

for i in range(2, X + 1):
    
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5] + 1)
    print(dp)
print(dp[X])



    
    