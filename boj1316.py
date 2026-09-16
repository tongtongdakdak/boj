n = int(input())
li = list()

for i in range(n):
    s = input()
    for j in range(len(s)):
        if s[j-1] == s[j]:
            li.append(s[j])
            if s[j] in li:
                li.remove(s[j])

print(li)