t = int(input())

def fibonacci(n):
    global count0
    global count1
    count0 = 0
    count1 = 0
    if n==0:
        count0 += 1
    elif n==1:
        count1 += 1
    else:
        return fibonacci(n-1)

if t >= 2:
    fibonacci(t)

print(count1, count0)