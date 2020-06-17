def printPrime(a):
    a.sort()
    big = a[len(a)-1]
    Primes = list(range(big))
    Primes[1] = 0
    i = 2
    while i <= big/2:
        j = i
        while i*j <big:
            Primes[i*j] = 0
            j+=1
        i+=1
    p = 0
    np = 0
    i = 0
    while i<len(a):
        if a[i] in Primes:
            p = p+a[i]
        else:
            np = np+a[i]
        i+=1
    print("소수의 합:",p)
    print("비소수의 합:",np)

b = True
a = []
while(b):
    N = int(input("정수입력(종료시는999): "))
    while N<2:
        print("2 이상의 수만 입력하세요 ")
        N = int(input("정수입력(종료시는999): "))
    if N == 999:
        break;
    else:
        a.append(N)
print("생성된 리스트:",a)
printPrime(a)
