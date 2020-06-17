import random
#######################################################
def printMatrix(A):
    i = 0
    j = 0
    while i<len(A):
        while j<len(A[0]):
            print(A[i][j],end=' ')
            j+=1
        print("")
        j = 0
        i+=1

#######################################################
A =[]
m = int(input("m = "))
n = int(input("n = "))
while m>0:
    count = 0
    a=[]
    while count<n:
        a.append(random.randint(0,5))
        count+=1
    A.append(a)
    m-=1
printMatrix(A)
