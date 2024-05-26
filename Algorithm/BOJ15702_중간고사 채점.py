"""
입력을 다 받아서 2중 for문으로 각 학생과 문제를 순회하면서
True가 숫자형으로는 1로 변하는 것을 이용해 각 문제가 맞았을 때 점수를 얻도록 하였고
총점을 내서 정렬을 한 뒤 가장 높은 점수, 가장 작은 학번을 출력하도록 하였음
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
score = list(map(int, input().split()))
students = [input().split() for _ in range(M)]
result = []
for i in range(M):
    total = 0
    for j in range(N):
        total += int(students[i][j+1] == 'O') * score[j]
    result.append((int(students[i][0]), total))
result.sort(key=lambda x: (x[1], -x[0]))
print(*result[-1])