# 백준 알고리즘 2920번 : 음계
asc=[1, 2, 3, 4, 5, 6, 7, 8]
des=[8, 7, 6, 5, 4, 3, 2, 1]
myls=list(map(int, input().split()))

if(myls==asc):
    print("ascending")
elif(myls==des):
    print("descending")
else:
    print("mixed")