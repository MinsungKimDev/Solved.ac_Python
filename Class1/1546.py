# 백준 알고리즘 1546번 : 평균
n = int(input())
a = list(map(int, input().split()))
b=[]

for i in range(n):
    b.append(a[i]/max(a)*100)

print(sum(b)/n)