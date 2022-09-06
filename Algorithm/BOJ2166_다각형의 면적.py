'''
벡터의 외적의 성질을 이용하여 너비를 계산함
(외적을 이용하지 않을 경우 꼬여있는 도형을 고려하지 않으므로 정확한 값이 나오지 않음)
2차원 벡터의 경우 벡터의 D가 외적의 크기와 일치하므로 그대로 사용
첫번째로 주어지는 점을 기준으로 
2번째 3번째 점과 이루는 삼각형, 
3번째 4번째 점과 이루는 삼각형... 의 과정으로 너비를 합산함
최종 출력시 f-string(포매팅)으로 자연스럽게 반올림하였음
순서가 역방향일 때 음수 너비가 나와서 abs함수를 이용해 양수만 나오도록 처리하였음
'''

import sys
input = sys.stdin.readline
N = int(input())

shape = []
total_width = 0
for i in range(N):
    shape.append(list(map(int, input().split())))
    if i >= 2:
        x1, y1 = shape[0]
        x2, y2 = shape[i]
        x3, y3 = shape[i-1]
        v1 = [x2-x1, y2-y1]
        v2 = [x3-x1, y3-y1]
        width = (v1[0]*v2[1] - v1[1]*v2[0])/2.0
        total_width += width

print(f'{abs(total_width):.1f}')