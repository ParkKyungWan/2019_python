# 4번 문제

def isPerfect(x):
    i = 1
    temp = 0
    while i< x:
        if x%i == 0:
            temp += i
        i += 1
    if i == temp:
        return 1
    elif i<temp:
        return 2
    elif i>temp:
        return 3


a = int(input('a = '))
while a <=0:
    a = int(input('a = '))
b = int(input('b = '))
while b <=0:
    b = int(input('b = '))

while a<=b:
    if isPerfect(a) == 1:
        print(a,": 완전수")
    elif isPerfect(a) == 2:
        print(a,": 과잉수")
    elif isPerfect(a) == 3:
        print(a,": 부족수")
    a+=1
