n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    if i==0:
        Min = a[i] 
        Max = a[i]
    else:
        if a[i] < Min:
            Min = a[i]
        elif a[i] > Max:
            Max = a[i]
print((int(Min)),(int(Max)))