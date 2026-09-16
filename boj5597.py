li = list()
li_input = list()

for i in range(1,30+1):
    li.append(i)

for j in range(1,28+1):
    j = int(input())
    li_input.append(j)

missing_num = list(set(li) - set(li_input))

if missing_num[0] > missing_num[1]:
    print(missing_num[1])
    print(missing_num[0])
    
else:
    print(missing_num[0])
    print(missing_num[1])