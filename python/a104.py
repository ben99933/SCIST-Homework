from sys import stdin


while(True):
    try:
        n = int(input())
        l = []
        s = input().split(" ")
        for i in range(n):
            l.append(int(s[i]))
        ans = sorted(l)
        for i in range(n):
            print(str(ans[i]) + " ",end='')
        print()
    except EOFError:
        exit()
