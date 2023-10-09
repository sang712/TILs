"""
누적합처럼 풀면 되는 문제인데 범위가 너무 넓어서 딕셔너리에 저장하였음
저장할 땐 시작하는 시각에 1을 더하고, 끝나는 시각에 1을 빼는 방식을 이용했고
이로인해 같은 시각에 끝나고 시작하는 과목을 중복처리할 수 있었음
"""
import sys
input = sys.stdin.readline

N = int(input())
lectures = {}
for _ in range(N):
	_, start, end = map(int, input().split())
	lectures.setdefault(start, 0)
	lectures[start] += 1
	lectures.setdefault(end, 0)
	lectures[end] -= 1

classroom = 0
max_classroom = 0
for _, lecture in sorted(list(lectures.items()), key=lambda x: x[0]):
    classroom += lecture
    if max_classroom < classroom:
        max_classroom = classroom
print(max_classroom)
