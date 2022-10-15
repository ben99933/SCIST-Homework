from sys import stdin
while(True):
    try:
        num = int(input())
        print("YES" if num%3==0 else "NO")
    except EOFError:
        exit()
