def winner(a, b):
    if a==b:
        return 3
    rule=["가위","바위","보"]
    i = 0
    while i<len(rule):
        if rule[i] == a:
            if rule[(i+1)%3]==b:
                return 2
            return 1
        i+=1


A = input("A선택\nA: ")
while A !="가위" and A!="바위" and A!="보":
    A = input("가위,바위,보만 입력하세요.\nA: ")

B = input("B선택\nB: ")
while B !="가위" and B!="바위" and B!="보":
    B = input("가위,바위,보만 입력하세요.\nB: ")

result = winner(A,B)
if result == 1:
    print("A 승")
elif result ==2:
    print("B 승")
else:
    print("무승부")
