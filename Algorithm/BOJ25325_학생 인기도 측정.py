"""
학생별로 투표수를 카운팅하여 졍렬한 뒤 출력하였음
"""
import sys
input = sys.stdin.readline

n = int(input())
votes = {student: 0 for student in input().split()}
for _ in range(n):
    for student in input().split():
        votes[student] += 1
for student, vote in sorted(votes.items(), key=lambda x: (-x[1], x[0])):
    print(student, vote)