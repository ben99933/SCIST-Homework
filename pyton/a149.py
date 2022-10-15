t = int(input())
while(t>0):
    t-=1
    s = input()
    sum = 1
    for i in range(len(s)):
        num = int(s[i])
        sum *= num
    print(sum)

