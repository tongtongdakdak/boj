li=[]
str=''
for i in range(5):
    li.append(input())

Max = max(len(j) for j in li) #최댓값 저장

for i in range(Max):
    for j in li:
        if i<len(j):
            str += j[i]

print(str)