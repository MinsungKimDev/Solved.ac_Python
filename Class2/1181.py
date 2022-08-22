# 백준 알고리즘 1181번 : 단어 정렬
n = int(input())
arr=[]
for i in range(0,n):
    arr.append(input())
myset = set(arr)
arr = list(myset)
arr.sort()
arr.sort(key=len)
for i in range(0, len(arr)):
    print(arr[i])