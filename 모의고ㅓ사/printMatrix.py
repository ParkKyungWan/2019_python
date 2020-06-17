import random
def printMatrix(A):
    y = 0
    a = [0,0,0]
    while y<A:
        x = 0
        while x <A:
            i = random.randint(0,2)
            print(i,end='')
            if i<1:
                a[0] += 1
            elif i>1:
                a[2] +=1
            else:
                a[1]+=1
            x+=1
        y +=1
        print("")
    print("0:",a[0])
    print("1:",a[1])
    print("2:",a[2])

N = int(input("N = "))
print("")
printMatrix(N)