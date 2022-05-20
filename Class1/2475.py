# 백준 알고리즘 2475번 : 검증수
a=list(map(int, input().split()))
mysum=0

for i in range(len(a)):
    mysum+=a[i] ** 2

print(mysum%10)