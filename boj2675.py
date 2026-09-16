T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    P = str()
    for j in range(len(S)):
        P += R*S[j]
    print(P)