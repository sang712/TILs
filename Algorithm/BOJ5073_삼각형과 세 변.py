"""
while문으로 반복해서 입력을 받고 조건을 확인하여 해당 조건에 맞는 결과를 출력하도록 하였음
0 0 0을 입력으로 받을 때 while문을 탈출하도록 함
"""
import sys
input = sys.stdin.readline

while True:
    triangle = list(map(int, input().split()))
    triangle.sort()
    if triangle[0] == triangle[1] == triangle[2] == 0:
        break
    if triangle[0] + triangle[1] <= triangle[2]:
        print('Invalid')
    elif triangle[0] == triangle[1] == triangle[2]:
            print('Equilateral')
    elif triangle[1] == triangle[0] or triangle[1] == triangle[2]:
        print('Isosceles')
    else:
        print('Scalene')