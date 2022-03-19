#이진 탐색(Binary Search)
#   배열내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
#   이진 탐색은 변수 3개 사용 찾으려는 범위의 시작점, 끝점, 중간점
#   찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교

#이진 탐색 소스코드 구현(재귀 함수)

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, (mid - 1))
    else:
        return binary_search(array, target, (mid + 1), end)

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, (n - 1))
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)

#반복문으로 구현한 이진 탐색 소스코드

def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search2(array, target, 0, (n - 1))
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)
