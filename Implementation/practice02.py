#구현 시각
from sys import stdin

N = int(stdin.readline())

count = 0

for hour in range(0, N + 1):
    for minute in range(0, 60):
        for second in range(0, 60):
            if '3' in str(second) or '3' in str(minute) or '3' in str(hour):
                print(str(hour), str(second), str(minute))
                count += 1
            
print(count)

