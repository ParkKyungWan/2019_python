import random
#######################################################
def minusMatrix(A):
    i = 0
    j = 0
    right = 0
    left =  0
    while i<len(A):
        while j<len(A):
            if i>j:
                left+=A[i][j]
            else:
                right+=A[i][j]
            j+=1
        i+=1
        j = 0
    if right>left:
        return right-left
    else:
        return left-right

#######################################################
n = int(input("n = "))
A = []
count_y = 0
while count_y<n:
    count_x = 0
    a=[]
    while count_x<n:
        if count_x == count_y:
            a.append(0)
        else:
            rand = random.randint(0,5)
            a.append(rand)
        count_x+=1
    A.append(a)
    count_y+=1
i = 0
j = 0
while i<len(A):
    while j<len(A[0]):
        print(A[i][j],end=' ')
        j+=1
    print("")
    j = 0
    i+=1
print("차:",minusMatrix(A))
