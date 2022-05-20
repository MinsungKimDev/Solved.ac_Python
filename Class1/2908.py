# 백준 알고리즘 2908번 : 상수
a=list(map(int, input().split()))
for i in range(len(a)):
    a[i]=int(str(a[i])[::-1])

print(max(a))