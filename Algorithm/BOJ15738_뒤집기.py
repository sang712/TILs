"""
문제가 준 대로 파이썬의 리스트 슬라이싱을 이용해서 자르고 뒤집으려고 했는데 시간초과가 나서
간단 버전으로 구하려고 하는 부분만 계산하도록 하였음
주어진 인덱스까지 중앙을 기준으로 뒤집히기 때문에
인덱스가 짝수일 때와 홀수일 때의 경우가 다르다고 생각했었는데
첫 값과 끝 값을 더한 값에서 주어진 인덱스 값을 빼면 쉽게 구할 수 있어서 해당 방법을 사용하였음
"""
import sys
input = sys.stdin.readline

N, K, M = map(int, input().split())
_ = input()
A = list(range(1, N+1))
for _ in range(M):
    i = int(input())
    if i > 0:
        if K <= i:
            standard = 1+i
            K = standard - K
    else:
        if K > N+i:
            standard = 2*N+i+1
            K = standard - K
print(K)
