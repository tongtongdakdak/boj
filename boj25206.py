total_score = 0
total_sum = 0

grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0','F']
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

for _ in range(20):
    a, b, c = input().split()
    b = int(float(b))
    for i in range(len(grade)):
        if c == 'P':
            continue
        total_score += b * float(score[grade.index(c)])
        total_sum += b

print(total_score / total_sum)