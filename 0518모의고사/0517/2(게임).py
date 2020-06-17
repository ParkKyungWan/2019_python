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
import random
c = ["가위", "바위", "보"]
A = input("선택: ")
while A !="가위" and A!="바위" and A!="보":
    A = input("가위,바위,보만 입력하세요: ")
B = random.choice(c)
print("컴퓨터는",B,"를 선택했습니다")
result = winner(A,B)
if result == 1:
    print("당신 승")
elif result ==2:
    print("컴퓨터 승")
else:
    print("무승부")

