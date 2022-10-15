t = int(input())
while(t>0):
    t -= 1
    array = input().split(" ")
    length = len(array)
    last = int(array[length-1])
    last2 = int(array[length-2])
    last3 = int(array[length-3])
    if(last-last2 == last2-last3):
        d = last-last2
        for i in range(length): print(array[i] + " ",end='')
        print(last + d)
    else:
        r = last//last2
        for i in range(length): print(array[i] + " ", end='')
        print(last*r)
