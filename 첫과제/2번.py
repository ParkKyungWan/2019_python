N = int(input('N = '))
while N<=0:
    N = int(input('N = '))
    
EnterPoint = 1
i = 1
while i< N+1:
    print(i,end=' ')
    if i == EnterPoint:
        print('\n',end='')
        EnterPoint = EnterPoint*2+1
    i+=1
    
