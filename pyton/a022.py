from sys import stdin


while(True):
    try:
        s = input()
        if(len(s)==0): break
        re = s[::-1]
        print("yes"if s==re else "no")
    except EOFError:
        exit()
