import random
def printRatio(n,minValue,maxValue):
    i = 0
    a = []
    while i <= maxValue-minValue:
        a.append(0)
        i+=1
    i = 0
    while i < n:
        r = random.randint(minValue,maxValue)
        a[r-minValue] +=1
        i += 1
    i = minValue
    print("난수    빈도수    비율")
    print("=====================")
    while i <= maxValue:
        print(i,"   ",a[i-minValue],"   ",str(a[i-minValue]/n*100)+"%")
        i+=1
N = int(input("N = "))
MIN = int(input("MIN = "))
MAX = int(input("MAX = "))
printRatio(N,MIN,MAX)