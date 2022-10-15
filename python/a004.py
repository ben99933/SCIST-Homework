from sys import stdin
while(True):
    try:
        num = int(input())
        if((num%4==0 and num%100!=0)or(num%400==0)): print("閏年")
        else: print("平年")
    except EOFError:
        exit()
