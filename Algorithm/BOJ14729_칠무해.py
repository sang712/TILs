"""
정렬하여 7개를 출력하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
grades = sorted([float(input()) for _ in range(N)])
for i in range(7):
    print(f'{grades[i]:.3f}')