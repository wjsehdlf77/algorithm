#큐와 스택

# from collections import deque

# a = [1, 2, 3, 4, 5]

# q = deque(a)

# print(q)

# print(list(q))

# deque는 스택과 큐의 장점을 채택한 것인데 데이터를 넣고 빼는 속도가 리스트 자료형에 비해
#효율적이며 queue 라이브러리를 사용하는 것보다 더 간단

#재귀함수

# def recursive_function(i):
#     if i == 100:
#         return
#     print(i, '번째 재귀 함수에서', i+1,'번쩨 재귀 함수를 호출합니다.')
#     recursive_function(i + 1)
#     print(i, '번째 재귀함수를 종료합니다')

# recursive_function(1)

#반복적으로 구현한 n!
# def factorial_iterative(n):

#     result = 1

#     for i in range(1, n + 1):
#         result *= i
#     return result

# print(factorial_iterative(5))

#재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1

    return n * factorial_recursive(n - 1)

print(factorial_recursive(7))

