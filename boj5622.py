s = input()
n = 0


for i in range(len(s)):
    time = ord(s[i]) - 64
    #A = 65
    if time <= 3:
        n += 3
    elif time <= 6:
        n += 4
    elif time <= 9:
        n += 5
    elif time <= 12:
        n += 6
    elif time <= 15:
        n += 7
    elif time <= 19:
        n += 8
    elif time <= 22:
        n += 9
    elif time <= 26:
        n += 10

print(n)