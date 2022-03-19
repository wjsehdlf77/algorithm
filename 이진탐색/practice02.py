#떡볶이 떡 만들기

from sys import stdin

#내방식은 끝에서 부터 -1씩 줄여가면서 탐색하므로 이진탐색으로 반반씩 줄여가는 것에 비해 시간이 훨씬 오래 걸릴것이다

# def max_height(array, max, client):
#     lambda_height = lambda x : x- max if x > max else 0
#     sum_height = sum(map(lambda_height, array))
    
#     if sum_height >= client:
#         return max
#     else:
#         return max_height(array, max - 1, client)
    

# N, M = map(int, stdin.readline().split())

# data = list(map(int, stdin.readline().split()))

# data.sort()

# max_data = max(data)

# print(max_height(data, max_data, M))

#이진탐색 재귀형식으로 구현했지만 M값이 딱 나누어 떨어지지 않는 경우는 0이 리턴된다 
# def max_height(array, start, end, client):
#     if start > end:
#         return 0
#     mid = (start + end) // 2

#     lambda_height = lambda x : x- mid if x > mid else 0
#     sum_height = sum(map(lambda_height, array))
    
#     if sum_height == client:
#         return mid
#     elif sum_height > client:
#         return max_height(array, mid + 1, end, client)
#     else:
#         return max_height(array, start, mid - 1, client)
    

# N, M = map(int, stdin.readline().split())

# data = list(map(int, stdin.readline().split()))

# data.sort()

# print(max_height(data, 0, max(data), M))











# 4 6
# 19 15 10 17

# 10 20
# 23 12 24 21 30 5 2 7 15 17