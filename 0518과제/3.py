import random
#######################################################
def addMatrix(A, B):
    C = []
    i = 0
    j = 0
    while i<len(A):
        c = []
        while j<len(A[0]):
            c.append(A[i][j]+B[i][j])
            j+=1
        i+=1
        j =0
        C.append(c)
    return C


#######################################################
m = int(input("m = "))
n = int(input("n = "))
A = []
B = []
Ap = ""
Bp = ""
while m > 0:
    _A = []
    _B = []
    count = 0
    while count < n:
        a = random.randint(0,5)
        Ap+=str(a)+" "
        b = random.randint(0,5)
        Bp+=str(b)+" "
        _A.append(a)
        _B.append(b)
        count += 1
    A.append(_A)
    Ap +="\n"
    Bp +="\n"
    B.append(_B)
    m -= 1
print("행렬 A")
print(Ap)
print("행렬 B")
print(Bp)
print("A+B")
for i in addMatrix(A,B):
    for j in i:
        print(j,end= ' ')
    print("")
