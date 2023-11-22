"""
f-스트링에서 float로 바로 반올림하는 것이 모두 정답이 나오는 건 아니라는 것을 알게 되었음
"""
N = int(input())
scores = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
          'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
          'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
          'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
          'F': 0.0}
total_score = 0
total_credit = 0
for _ in range(N):
    subject, credit, score = input().split()
    total_score += int(credit) * scores[score]
    total_credit += int(credit)
    
ans = int(total_score / total_credit * 100 + 0.5)
print(f'{ans/100:.2f}')