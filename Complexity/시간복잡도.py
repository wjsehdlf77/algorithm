#시간복잡도 : 알고리즘을 위해 필요한 연산의 횟수
#시간복잡도는 빅오(big-O)표기법을 따른다

#O(N)
#연산의 횟수는 상대적으로 N이 커짐에 따라서 무시할 수 있을 정도로 작아지므로 가장 영향력이 큰 부분은 N
array = [3, 5, 1, 2, 4] #5개의 데이타 (N = 5)
summary = 0             #합계를 저장할 변수

#모든 데이터를 하나씩 확인하며 합계를 계산
for x in array:
    summary += x

print(summary)

#상수연산이므로
#O(1)

a = 5
b = 7

print(a + b)

#대입연산과 출력함수를 무시한다고 보면 연산횟수는 1회

#O(N^2)
for i in array:
    for j in array:
        temp = i * j
        print(temp)

#코딩테스트에선 O(N^3)을 넘어가면 안된다

#일반적으로 문재를 풀때 예시 시간제한이 1초인 경우

#   N의 범위가 500 -> O(N^3)
#   N의 범위가 2000 -> O(N^2)
#   N의 범위가 100,000 -> O(NlogN)
#   N의 범위가 10,000,000 -> O(N)

