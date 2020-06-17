def delDup(s):
    answer = ""
    for i in range(0,len(s)):
        if answer.count(s[i])<1:
            answer+=s[i]
    return answer
print(delDup(input('s=')))
