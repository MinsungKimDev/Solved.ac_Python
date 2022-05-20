# 백준 알고리즘 1157번 : 단어공부
a=input()
a=a.lower()
b=list(set(a))
mycount=[]

for i in range(len(b)):
    mycount.append(a.count(b[i]))

if mycount.count(max(mycount)) > 1:
    print("?")
else:
    print(b[mycount.index(max(mycount))].upper())