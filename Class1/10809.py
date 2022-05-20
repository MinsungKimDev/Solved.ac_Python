# 백준 알고리즘 10809번 : 알파벳 찾기
s=input()

for i in range(97,123):
    if s.count(chr(i)) > 0:
        print("%s "%s.index(chr(i)) ,end='')
    else:
        print("-1 ", end='')