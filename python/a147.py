import sys
from sys import stdin
while(True):
    num = int(input())
    if(num==0): exit()
    for i in range(num):
        if(i%7!=0): print(str(i) + " ",end='')
    print("")

