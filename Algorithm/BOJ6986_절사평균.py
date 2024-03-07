"""
문제의 데이터가 의도하길 float형(혹은 double형)을 사용하면 오차가 나게 되어있어서
오차의 값을 없애기 위해 0.0000001 10e-7을 더해주었음
10e-6부터는 틀린답을 냄
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

scores = [float(input()) for _ in range(N)]
scores.sort()
print(f'{sum(scores[K:N-K])/(N-2*K) + 0.0000001:.2f}')
print(f'{(K*scores[K] + sum(scores[K:N-K]) + scores[N-K-1]*K)/N + 0.0000001:.2f}')