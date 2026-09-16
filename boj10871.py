n,x = map(int, input().split())
a = list(input().split())
l = list()
for i in range(n):
    if int(a[i]) >= x:
        continue 
    else:
        l.append(a[i])
    
print(*l)