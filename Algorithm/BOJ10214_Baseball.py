'''
요구사항대로 구현하였음
input의 line수가 많아 sys를 사용하여
120ms 에서 72ms로 시간을 단축할 수 있었음
'''
import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    Y, K = 0, 0
    for i in range(9):
        score = list(map(int, input().split()))
        Y += score[0]
        K += score[1]
        
    if Y > K:
        print("Yonsei")
    elif K > Y:
        print("Korea")
    else:
        print("Draw")