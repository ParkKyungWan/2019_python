def twosum(a,n):
    b = []
    if len(a)%2 != 0:
        a.append(0)
        n+=1
    i = 0
    j = 1
    while j<=n:
        b.append(a[i]+a[j])
        i +=2
        j+=2

    return b
import random
N = int(input("N = "))
i = 0
a = []
while i<N:
    a.append(random.randint(1,5))
    i+=1
print("a = ",a)
print("b = ",twosum(a,N-1))