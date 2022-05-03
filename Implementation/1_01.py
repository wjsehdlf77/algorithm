#럭키 스트레이트


#내가푼 방법
from sys import stdin

score = stdin.readline().rstrip()

right = []
left = []

score_list = [n for n in score]

length = len(score_list)//2

for i in range(length):
    left.append(int(score_list[i]))
    right.append(int(score_list[i + length]))

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")



#답안
n = input()

length = len(n)
summary = 0

for i in range(length//2):
    summary += int(n[i])

for i in range(length // 2, length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")



