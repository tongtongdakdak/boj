str = input().upper()
li = list()

for i in range(26):
    li.append(str.count(chr(i+65)))

max = max(li)

print(li)