N,M = map(int,input().split())

li = []

for a in range(1,N+1):
    li.append(a)

for b in range(M):
    i,j = map(int,input().split())
    li[i-1],li[j-1] = li[j-1],li[i-1]

print(*li)