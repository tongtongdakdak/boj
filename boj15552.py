import sys

t = sys.stdin.readline().rstrip()
for i in range(int(t)):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)