"""
문제에서 요구하는 대로 분기를 나누어 출력을 하도록 하였음
"""
import sys
input = sys.stdin.readline

while True:
    num1, num2 = map(int, input().split())
    if num1 == num2:
        break

    if num1 > num2 and num1 % num2 == 0:
        print('multiple')
    elif num1 < num2 and num2 % num1 == 0:
        print('factor')
    else:
        print('neither')