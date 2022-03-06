#수행 시간 측정 소스 코드

import time
from random import randint


start_time = time.time()

#프로그램 소스코드

end_time = time.time()

print(end_time - start_time)


#선택 정렬과 기본 정렬 라이브러리의 수행 시간 비교



array = []

for _ in range(10000):
    array.append(randint(1, 100))

#선택 정렬 프로그램 성능 측정
start_time = time.time()

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

    #여기가 스와프 하는 곳
    array[i], array[min_index] = array[min_index], array[i]

end_time = time.time()
total_time = end_time - start_time

print(f"선택 정렬 성능 측정 : {total_time}")


#기본 정렬 라이브러리 성능 측정

start_time = time.time()

array.sort()

end_time = time.time()
total_time = end_time - start_time

print(f"기본 정렬 라이브러리 성능 측정 : {total_time}")

