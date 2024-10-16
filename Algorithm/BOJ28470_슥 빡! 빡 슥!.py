"""
그냥 쉬운 문제인 줄 알았는데
부동소수점 문제로 floor 연산(int함수로 대신함)할 때 
정확한 답을 얻지 못하는 문제가 있음
그래서 10을 곱한 뒤 10으로 나누는 방법으로 문제를 해결함
"""
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
K = list(map(float, input().split()))
adrenaline = 0
for i in range(N):
    K[i] *= 10
    if K[i] >= 10:
        A[i] = int(A[i] * K[i] // 10)
    else:
        B[i] = int(B[i] * K[i] // 10)
    adrenaline += A[i] - B[i]
print(adrenaline)
