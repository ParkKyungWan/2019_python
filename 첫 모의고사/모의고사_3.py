# 3번 문제

def isPrime(x):
    i = 2
    while i<= x/2:
        if x%i == 0:
            return False
        i += 1
    return True

N = int(input('N = '))
i = 2
while i<=N:
    if isPrime(i):
        print(i,end=' ')
    i+=1
