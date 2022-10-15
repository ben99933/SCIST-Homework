from sys import stdin

def gcd(a,b):
    if(b>a): return gcd(b,a)
    if(a%b==0): return b
    return gcd(b,a%b)

while(True):
    try:
        s = input().split(" ")
        a = int(s[0])
        b = int(s[1])
        print(gcd(a,b))
    except EOFError:
        exit()
