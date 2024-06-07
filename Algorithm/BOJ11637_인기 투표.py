"""
과반수가 절반을 포함하지 않는 인원수라는 점을 알게 되었음
인덱스 번호로 평균을 구한 것과 절반이 아니라 평균을 구한 것
과반에 절반을 포함 한 점 등의 실수를 해서 4번만에 정답을 받아냄
"""
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    students = [(i, int(input())) for i in range(n)]
    mean = sum(map(lambda x: x[1], students)) / 2
    students.sort(key=lambda x: x[1])
    if students[-1][1] == students[-2][1]:
        print('no winner')
    elif students[-1][1] > mean:
        print(f'majority winner {students[-1][0] + 1}')
    else:
        print(f'minority winner {students[-1][0] + 1}')