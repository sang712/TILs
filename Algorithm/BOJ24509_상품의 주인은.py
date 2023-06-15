"""
각 과목별로 정렬을 하여 1등을 계산하고
만약에 1등이 상을 받았다면 무시하고 다음 사람을 선택하는 방식으로 문제를 풀이하였음
"""
import sys
input = sys.stdin.readline

N = int(input())

students = []
for _ in range(N):
    students.append(list(map(int, input().split())))

winner = []

for i in range(1, 5):
    students.sort(key=lambda x: (-x[i], x[0]))
    for student in students:
        if student[0] in winner:
            continue
        winner.append(student[0])
        break

print(*winner)