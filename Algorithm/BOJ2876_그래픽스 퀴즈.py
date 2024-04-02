"""
문제가 이해하기 어려웠는데
연속한 책상에서 각각 한 명의 학생을 선택하고 모두 같은 그레이드를 주는 것을 찾는 것이므로
점수를 줄 수 없는 경우가 없어야 한다는 뜻이었음
그래서 가장 길게 연속된 점수를 찾아서 출력하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
desks = [list(map(int, input().split())) for _ in range(N)]
max_serial = 0
grade = 0
for i in range(1, 6):
    serial = 0
    for j in range(N):
        if desks[j][0] == i or desks[j][1] == i:
            serial += 1
        else:
            serial = 0
        if serial > max_serial:
            max_serial = serial
            grade = i
print(max_serial, grade)