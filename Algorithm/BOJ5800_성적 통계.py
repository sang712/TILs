"""
문제에서 요구하는 사항을 그대로 구현하였음
"""
import sys
input = sys.stdin.readline

K = int(input())
for k in range(1, K + 1):
    N, *scores = map(int, input().split())
    scores.sort()
    
    max_score = scores[-1]
    min_score = scores[0]
    largest_gap = 0
    for i in range(1, len(scores)):
        if largest_gap < scores[i] - scores[i - 1]:
            largest_gap = scores[i] - scores[i - 1]
    
    print(f'Class {k}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {largest_gap}')