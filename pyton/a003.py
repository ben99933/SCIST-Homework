st = input().split(" ")
a = int(st[0])
b = int(st[1])
s = (a*2 + b)%3
print("普通" if s == 0 else "吉" if s==1 else "大吉")

