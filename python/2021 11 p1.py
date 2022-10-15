from sys import stdin
n = input()

li = []
s = input().split(" ")
count = 0

length = len(s)

for i in range(length):
    num = int(s[i])
    li.append(num)

for i in range(length):
    if(i == 0 and li[0]==0):
        li[0] = li[1]
        count += li[1]
    if(li[i]==0)and (1<=i<length-1):
        if(li[i-1]>li[i+1]):
            li[i] = li[i+1]
            count+=li[i]
        else:
            li[i] = li[i-1]
            count+= li[i-1]

    if(i == length-1)and li[i] ==0:
        li[i] = li[i-1]
        count += li[i-1]
print(count)
