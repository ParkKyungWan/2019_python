# 2번 문제

a = int(input('a = '))
while a <=0:
    a = int(input('a = '))
b = int(input('b = '))
while b <=0:
    b = int(input('b = '))

if a>b:
    a,b = b,a
while a<b:
    print("섭씨:",a,"화씨:",a*9/5+32)
    a +=5
    
