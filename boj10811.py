n, m = map(int, input().split())
li = []

for a in range(1, n + 1):
    li.append(a)

for b in range(m):
    i, j = map(int, input().split())
    li[i-1:j] = li[i-1:j][::-1]

print(*li)
