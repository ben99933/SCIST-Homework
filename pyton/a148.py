from sys import stdin


while(True):
    try:
        s = input().split(" ")
        n = int(s[0])
        sum = 0
        for i in range(1, len(s)):
            sum += int(s[i])
        if(sum > 59*n): print("no")
        else: print("yes")
    except EOFError:
        exit()

        
