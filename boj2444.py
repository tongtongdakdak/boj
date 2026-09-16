N = int(input())
s = '*'

for i in range(2 * N - 1):
    if i < N:
        print((N - i - 1) * ' ' + (2 * i + 1) * s)
    else:
        print((i - N + 1) * ' ' + (2 * (2 * N - i - 2) + 1) * s)