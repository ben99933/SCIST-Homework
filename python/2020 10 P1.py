s = input().split(" ")
n = int(s[0])
d = int(s[1])
count = 0
sum = 0
for i in range(n):
    s = input().split(" ")
    mn = 0x7fffffff
    mx = -1
    for j in range(len(s)):
        num = int(s[j])
        if(num>mx): mx = num
        if(mn> num): mn = num
    if(mx-mn)>=d :
        count+=1
        sum += ((int(s[0]) + int(s[1]) + int(s[2]))//3)
print(count, sum)
