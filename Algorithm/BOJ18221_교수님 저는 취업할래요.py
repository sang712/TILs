"""
우선 입력을 받으면서 교수님과 승규의 위치를 찾을 수 있도록 하였고
입력의 크기가 최대 1000 * 1000 이라 생각보다 탐색이 오래걸리므로
한 번 찾은 경우에는 더이상 탐색하지 않도록 조건을 걸어주었음

그리고 오차를 제거하기 위해 굳이 거리는 루트를 적용하지 않고 그냥 제곱의 합을 그대로 사용하였고
2중 for문 대신 1중 for문에 리스트 슬라이싱 및 리스트 내장 함수인 카운트 함수를 이용하였음

시간 100ms로 python 언어 전체에서 1등 속도를 달성하였음
2등은 140ms으로 꽤나 큰 차이인 듯함
다만 문제를 푼 사람이 400여명이라
"""
import sys
input = sys.stdin.readline

N = int(input())
classroom = []
prof = sg = None
for i in range(N):
    row = input().split()
    if not prof and '5' in row:
        prof = (i, row.index('5'))
    if not sg and '2' in row:
        sg = (i, row.index('2'))
    classroom.append(row)

dist_square = (prof[0] - sg[0]) ** 2 + (prof[1] - sg[1]) ** 2

if dist_square >= 25:
    num_students = 0
    for r in range(min(prof[0], sg[0]), max(prof[0], sg[0]) + 1):
        num_students += classroom[r][min(prof[1], sg[1]):max(prof[1], sg[1]) + 1].count('1')
    if num_students >= 3:
        print(1)
    else:
        print(0)
else:
    print(0)
