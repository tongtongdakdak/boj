x = int(input())

diag = 1
while x > diag:
    x -= diag
    diag += 1
    
if diag % 2 == 1:
    a = diag - x+1
    b = x
    
else:
    a = x
    b = diag -x+1

print(f"{a}/{b}")