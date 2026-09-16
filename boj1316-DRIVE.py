n = int(input())
li = list()
cnt = 0

for i in range(n):
    word = input()
    back = ' '
    use = []
    group = True
    
    for j in word:
        if j != back:
            if j in use:
                group = False
                break
            use.append(j)
        back = j
    
    if group == True:
        cnt += 1

print(cnt)