# 백준 알고리즘 2439번 : 별 찍기 - 2
n = int(input())

for i in range(n):
    i += 1
    print(" " * (n-i) + "*" * i)