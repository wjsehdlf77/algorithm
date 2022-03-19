#다이나믹 프로그래밍(dynamic programming)
#   큰문제를 작은 문제로 나눌 수 있다
#   작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일
#   메모이제이션(Memoization)기법을 사용해서 한번 푼 문제를 저장해 놓고 반복되면 저장값만 리턴한다


#피보나치 함수 소스코드
def fibo(x):
    if x == 1 or x == 2:
        return 1

    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))

#피보나치 수열 소스코드(재귀적)
#큰 문제를 해결하기 위해 작은 문제를 호출한다고 하여 탑다운(Top-Down)방식
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))


#반복문을 이용하여 소스코드를 작성하는 경우 작은 문제부터 차근차근 답을 도출한다고 하여 Bottom-up방식

d = [0] * 100

#첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

#피보나치 함수 반복문으로 구현(보텀업 다이나믹 프로그래밍
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
