def minusMatrix(A):
    n=int(input('n='))
    l=1
    j=1
    e=0
    z=n
    k=1
    while n>=l:
        while z>=j:
            if j==k:
                A.append(0)
            else:
                A.append(random.randint(0,3))
            j+=1
            t=len(A)                
            while t>e:
                print(A[e],end=' ')
                e+=1
        print()
        l+=1
        j=1
        k+=1
import random
A=[]
minusMatrix(A)
