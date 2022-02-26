#greedy 곱하기 혹은 더하기

from sys import stdin

# data = [int(n) for n in str(stdin.readline().rstrip())]

# data.sort()

# total = 0

# for i in data:
    
#     total = max(total + i, total * i)

# print(total)

data = [int(n) for n in str(stdin.readline().rstrip())]

result = data[0]

for i in range(1, len(data)):
    num = data[i]
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
    