# 백준 알고리즘 2675번 : 문자열 반복
t=int(input())
mylist=[]

for i in range(t):
    a,b = map(str, input().split())
    mylist.append((a,b))
# print(mylist)

for i in range(t):
    result=[]
    for j in range(len(mylist[i][1])):
        result.append(mylist[i][1][j]*int(mylist[i][0]))
    result="".join(result)
    print(result)