
#선택정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

    #여기가 스와프 하는 곳
    array[i], array[min_index] = array[min_index], array[i]

print(array)

#시간복잡도가 O(N^2)
#선택정렬은 매우 비효율적
#가장 작은 데이터를 찾는 일이 코딩테스트에서 잦으므로 선택 정렬 소스코드 형태에 익숙해질 필요가 있다.
