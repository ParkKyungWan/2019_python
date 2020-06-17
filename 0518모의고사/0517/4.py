def countChar(s):
    a=[]
    for i in range(27):
        a.append(0)
    i = 0
    while i <len(s):
        if ord(s[i]) == 32:
            a[0]+=1
        else:
            a[ord(s[i])-64]+=1
        i+=1
    print(a)
s = input("문자열 입력: ")
countChar(s)
