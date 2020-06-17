def printMatrix(a):
    x = 1
    y = 0
    answer=0
    while y<len(a):
        while x<len(a[0]):
            if x>y:
                if a[x][y] == a[y][x]:
                    answer +=1
                x+=1
        y+=1
        x=1+y
    print("대칭인 원소의 개수 :",answer)

import random
n = int(input("n = "))
a = []
for i in range(n):
    nums = []
    for i2 in range(n):
        rand =random.randint(0,2)
        if i == i2:
            rand = 0
        nums.append(rand)
        print(rand,end=' ')

    a.append(nums)
    print("")
print(" ")
printMatrix(a)
