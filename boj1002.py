import math 

T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    dis_x = x1 - x2
    dis_y = y1 - y2
    distance = math.sqrt(dis_x*dis_x + dis_y*dis_y)
    
    if distance == 0 and r1 == r2:
        print(-1)
    elif distance == r1 + r2 or distance == abs(r1 - r2):
        print(1)
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)
    else:
        print(0)
