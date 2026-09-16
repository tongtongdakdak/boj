A,B = input().split()

A = A[::-1]
B = B[::-1]
A,B = int(A), int(B)
print(max(A,B))