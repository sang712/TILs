"""
입력 n이 0일 수도 있다는 점
n의 15% 의 반올림이 0일 때 list[0:0] = []라는 점을 간과하였다.
n의 15% 의 반올림이 1 이상이면 list[1:-1]
"""
import sys
input = sys.stdin.readline

n = int(input())

review = [int(input()) for _ in range(n)]
review.sort()

exclude = int(n * 0.15 + 0.5)
if n == 0:
    result = 0
elif exclude == 0:
    result = int(sum(review)/n + 0.5)
else:
    result = int(sum(review[exclude:-exclude]) / (n - 2*exclude) + 0.5) if n else 0

print(result)