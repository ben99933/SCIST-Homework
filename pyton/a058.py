t = int(input())
a = 0
b = 0
c = 0
while t!=0:
    t -= 1
    num = int(input())
    if num%3==0: a +=1
    elif (num-1)%3==0: b+=1
    else: c +=1
print(a, b, c)
