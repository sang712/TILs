"""
입력을 받아서 필요한 부분은 인트형으로 변환하고
문제에서 요구한대로 정렬을 한 뒤 이름만 뽑아 출력하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
students = []
for _ in range(N):
    name, *scores = input().split()
    students.append((name, *list(map(int, scores))))
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
ans = [s[0] for s in students]
print(*ans, sep='\n')