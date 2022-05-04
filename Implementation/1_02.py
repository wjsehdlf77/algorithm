#문자열 재정렬

# 48~57
#나의 방법
s = list(input())

s.sort()

count = 0
data = []

for i in range(len(s)):
    if ord(s[i]) >= 48 and ord(s[i]) <= 57:
        count += 1
        data.append(int(s[i]))
        

del s[0:count]
sum_data = str(sum(data))
s.append(sum_data)
print("".join(s))

#답안

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))






#K1KA5CB7

#AJKDLSI412K4JSJ9D