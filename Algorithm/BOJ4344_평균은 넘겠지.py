"""
2년전에 푼 문제 재채점 후 틀린 답이 되어 다시 풀이 하였음
이전 풀이에서는 마지막 답을 round했는데
이번 답은 그럴 필요없이 아예 출력에서 소수점 3째자리까지 출력하였음
"""
import sys
input = sys.stdin.readline
C = int(input())

for _ in range(C):
    num_students, *scores = list(map(int, input().split()))
    average = sum(scores) / num_students
    above_average = 0
    for score in scores:
        if score > average:
            above_average += 1
    
    print(f'{above_average * 100 / num_students:0.3f}%')
    