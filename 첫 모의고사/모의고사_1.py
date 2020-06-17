# 1번 문제

N = int(input('N = '))
if N<3:
    N = int(input('N = '))
i = 1
temp_i = 0
before = 0
while N>0:
    print(i,end=' ')
    temp_i = i
    i += before
    before = temp_i
    N -=1
    
