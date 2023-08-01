"""
우선 각 경우별로 유효한 값인지 확인을 한 뒤에 
유통기한이 지났는지 안 지났는지를 확인함
유통기한이 지났으면 바로 다음 입력으로 넘어가고 그렇지 않으면
set에 넣어서 모든 경우를 확인 한 뒤에 출력하도록 하였음
"""
import sys
input = sys.stdin.readline 

Y, M, D = map(int, input().split())
N = int(input())

last_day_of_month =[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
results = []
for _ in range(N):
    A, B, C = map(int, input().split())
    result = set()
    if 0 <= A <= 99 and 1 <= B <= 12:
        last_day = last_day_of_month[B] if not B == 2 or not A % 4 == 0 else 29
        if 1 <= C <= last_day:
            if Y < A or Y == A and (M < B or M == B and D <= C):
                result.add('safe')
            else:
                results.append('unsafe')
                continue
    
    if 0 <= C <= 99:
        if 1 <= B <= 12:
            last_day = last_day_of_month[B] if not B == 2 or not C % 4 == 0 else 29
            if 1 <= A <= last_day:
                if Y < C or Y == C and (M < B or M == B and D <= A):
                    result.add('safe')
                else:
                    results.append('unsafe')
                    continue
        
        if 1 <= A <= 12:
            last_day = last_day_of_month[A] if not A == 2 or not C % 4 == 0 else 29
            if 1 <= B <= last_day:
                if Y < C or Y == C and (M < A or M == A and D <= B):
                    result.add('safe')
                else:
                    results.append('unsafe')
                    continue
    results.append('safe') if 'safe' in result else results.append('invalid')

print(*results, sep='\n')