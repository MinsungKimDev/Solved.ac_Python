# 백준 알고리즘 1018번 : 체스판 다시 칠하기 
# 
# //////////실패///////////
import sys

n,m = map(int, input().split())
myls=[]
psum=0
psumarr=[]

for i in range(m):
    myls.append(sys.stdin.readline())

for i in range(m):
    for j in range(n):

for i in range(m):
    if(myls[i].count("W") == myls[i].count("B")):
        continue
    else:
        paint = 0
        paint = 4 - min(myls[i].count("W"), myls[i].count("B"))
        psum+=paint
    psumarr.append(psum)

print(min(psumarr))