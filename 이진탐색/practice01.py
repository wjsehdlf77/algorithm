from sys import stdin

#재귀함수사용
# def search(array, target, start, end):
#     if start > end:
#         return None
    
#     mid = (start + end) // 2

#     if array[mid] == target:
#         return True
#     elif array[mid] > target:
#         return search(array, target, start, mid - 1)
#     else:
#         return search(array, target, mid + 1, end)

    

# N = int(stdin.readline())
# sell_data = list(map(int, stdin.readline().split()))
# sell_data.sort() #이진탐색에서 배열의 정렬은 필수! 배열을 계속 반으로 갈라서 탐색함

# M = int(stdin.readline())
# buy_data = list(map(int, stdin.readline().split()))

# for buy in buy_data:
#     result = search(sell_data, buy, 0, N - 1)
#     if result != None:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')



def search2(array, target, start, end):
    while start <= end:             #while문은 조건이 true일때는 계속 돌다가 False로 바뀌면 break 헷갈리지마!
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

N = int(stdin.readline())
sell_data = list(map(int, stdin.readline().split()))
sell_data.sort() #이진탐색에서 배열의 정렬은 필수! 배열을 계속 반으로 갈라서 탐색함

M = int(stdin.readline())
buy_data = list(map(int, stdin.readline().split()))

for buy in buy_data:
    result = search2(sell_data, buy, 0, N - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
        







# 5
# 8 3 7 9 2
# 3
# 5 7 9