N = int(input())
li = list(map(int,input().split()))
Max = 0
sum = 0

Max = max(li)
    
for j in range(len(li)):
    sum += li[j]/Max * 100
    

print(sum/N)