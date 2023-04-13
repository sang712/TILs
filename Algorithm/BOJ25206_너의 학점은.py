"""
파이썬이라 입력을 나누기 편했고
문제에서 요구한대로 구현하였음
"""
score_table = {'A+': 4.5, 'A0': 4.0,
               'B+': 3.5, 'B0': 3.0,
               'C+': 2.5, 'C0': 2.0,
               'D+': 1.5, 'D0': 1.0,
               'F': 0.0}

num_subjects = 0
total_score = 0
for _ in range(20):
    subject, credit, score = input().split()
    if not score == 'P':
        num_subjects += float(credit)
        total_score += float(credit) * score_table[score]
        
print(f'{total_score / num_subjects:.6}')
