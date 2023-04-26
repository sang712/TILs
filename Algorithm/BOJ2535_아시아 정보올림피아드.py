"""
정렬한 뒤에 각 나라별 최대 2명이라는 규칙을 적용하여 출력하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
info = []
school = [0] * (N + 1)
for _ in range(N):
    sch_num, stu_num, score = map(int, input().split())
    info.append((sch_num, stu_num, score))
    
info.sort(key = lambda x: x[2])
cnt = 0
while cnt < 3:
    sch_num, stu_num, score = info.pop()
    if school[sch_num] < 2:
        school[sch_num] += 1
        cnt += 1
        print(sch_num, stu_num)