# 백준 알고리즘 11720번 : 숫자의 합
n=int(input())
s=input()
myls=[]
mysum=0

for i in range(n):
    myls.append(s[i])

for i in range(n):
    mysum+=int(myls[i])

print(mysum)