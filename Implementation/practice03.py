#구현문제 왕실의 나이트

from sys import stdin

# data = list(map(str, stdin.readline().rstrip()))
# data[1] = int(data[1])

# row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# column = [1, 2, 3, 4, 5, 6, 7, 8]

# r_num = row.index(data[0])
# c_num = column.index(data[1])

# steps = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2)]

# count = 0

# for r, c in steps:
#     nr = r_num + r
#     nc = c_num + c
#     if nr >= 8 or nc >= 8 or nr < 0 or nc < 0:
#         continue
#     count += 1

# print(count)

data = stdin.readline()
row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2)]

count = 0

for step in steps:
    next_row = row + step[0]
    nex_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and nex_column >= 1 and nex_column <= 8:
        count += 1

print(count)




