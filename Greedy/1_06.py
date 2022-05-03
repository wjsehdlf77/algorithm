#greedy 무지의 먹방 라이브
import heapq

def solution(food_times, k):
    result = 0
    q = []
    for item in enumerate(food_times, start=1):
        heapq.heappush(q, item)
        print(q)
    
    while k:
        index, food_time = heapq.heappop(q)
        if index != 3:
            index = index % 3
        if food_time != 0:
            food_time -= 1
            k -= 1
        result = index
        heapq.heappush(q, (index + 3 , food_time))
        
        
    return result

print(solution([3,1,2], 5))