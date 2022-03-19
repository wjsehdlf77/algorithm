#1로 만들기

from sys import stdin

def one(x):
    if x == 1:
        return 1
    if x % 1 != 0:
        return 
    return min(one(x/5), one(x/3), one(x/2), one(x - 1))

   
    

X = int(stdin.readline())


print(one(X))


    
    