S = input() #gpt도움받음
n = 0

for i in range(26):
    char = chr(ord('a') + i)
    print(S.find(char), end=' ')