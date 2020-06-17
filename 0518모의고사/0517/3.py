def makeNum(s):
    nums = []
    num =""
    i = 0
    stack = 0
    while i<len(s):
        if s[i]==" ":
            nums.append(int(num))
            stack += int(num)
            num=""
            i+=1
        else:
            num+=s[i]
            i+=1
    nums.append(int(num))
    stack += int(num)
    print("정수 리스트 :",nums,"\n정수 리스트의 합 :",stack)

def check(s):
    for i in s:
        if ord(i)!=32:
            if ord(i)< 48 or ord(i)>57:
                return False
    return True

s = input("s = ")
while not check(s):
    print("숫자와 띄어쓰기만 입력 가능합니다.")
    s = input("s = ")

makeNum(s)


