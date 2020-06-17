def minusMatrix(A):
    n=int(input('n='))
    l=1
    j=1
    e=0
    z=n
    k=1
    left = 0
    right = 0 
    while n>=l:
        while z>=j:
            if j==k:
                A.append(0)
            else:
                rand = random.randint(0,3)
                if j>k:
                    right +=rand
                else:
                    left += rand
                A.append(rand)
                
            j+=1
            t=len(A)                
            while t>e:
                print(A[e],end=' ')
                e+=1
        print()
        l+=1
        j=1
        k+=1
    if left>right:
        print("차:",left-right)
    else:
        print("차:",right-left)
import random
A=[]
minusMatrix(A)
