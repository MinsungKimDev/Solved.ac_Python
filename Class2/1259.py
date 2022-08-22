# 백준 알고리즘 1259번 : 팰린드롬수
while True:
    n = input()

    if n == '0':
        break

    if n != n[::-1]: # -> 문자열 뒤집기 ex) my_str = "김민성" 이라는 문자열이 있으면 뒤집은것 : my_str[::-1] = "성민김"
        print("no")
    else:
        print("yes")