li = list()
for i in range(10):
    a = int(input())
    a = a % 42
    li.append(a)

print(len(set(li)))