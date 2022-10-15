k = -7
s = input()
s2 = ""
for i in range(len(s)):
    asc = ord(s[i])
    asc +=k
    s2 = s2 + chr(asc)
print(s2)

