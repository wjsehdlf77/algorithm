#부품찾기 -> 계수정렬.ver


#내방법
from sys import stdin

# N = int(stdin.readline())
# sell_data = list(map(int, stdin.readline().split()))

# M = int(stdin.readline())
# buy_data = list(map(int, stdin.readline().split()))

# count = [0] * (max(sell_data) + 1)    부품수는 1<=N<=1,000,000 이므로 저장공간은 1,000,001이다
# count = [0] * 1000001

# for i in range(len(sell_data)):
#     count[sell_data[i]] += 1

# for i in buy_data:
#     if count[i] > 0:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

N = int(stdin.readline())
array = [0] * 1000001
for i in input().split():
    array[int(i)] = 1

M = int(stdin.readline())
buy_data = list(map(int, stdin.readline().split()))

for i in buy_data:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
