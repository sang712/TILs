"""
우선 전공과목부터 듣도록 하고 한 학기에 들을 수 있는 6과목을 모두 듣는 방식으로 계산함
"""
N, A, B = map(int, input().split())
semesters = [list(map(int, input().split())) for _ in range(10)]
for i in range(8-N):
    limit = 6
    a, b = semesters[i]
    A += a * 3
    B += a * 3
    limit -= a
    if limit > 0:
        rest = min(limit, b)
        B += rest * 3
if A >= 66 and B >= 130:
    print('Nice')
else:
    print('Nae ga wae')