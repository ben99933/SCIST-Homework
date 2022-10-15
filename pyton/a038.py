from sys import stdin


while(True):
    try:
        print(int(input()[::-1]))
    except EOFError:
        exit()
