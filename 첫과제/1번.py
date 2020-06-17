

a = int(input('a = '))
x = int(input('x = '))
e = int(input('e = '))
while e<0:
    e = int(input('e = '))
if e==0:
    answer = a
else:
    temp = x
    while e>1:
        x *=temp
        e-=1
    answer = a*x
        
print('계산 결과 :', answer)
