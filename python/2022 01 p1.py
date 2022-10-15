s1 = input().split(" ")
n = int(s1[0])
d = int(s1[1])
flag = True #擁有股票
s2 = input().split(" ")
x = 0
sum = 0
for  i in range(n):
    y = int(s2[i])
    if(x==0)or ((y <= x-d)and(flag == False)):
        x = y
        flag = True
    if(y>=(x+d)) and flag==True:
        sum += y-x
        x = y
        flag = False

print(sum)
