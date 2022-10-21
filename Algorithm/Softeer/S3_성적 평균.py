'''
조건
1 ≤ N ≤ 106 인 정수
1 ≤ K ≤ 104 인 정수
1 ≤ Si ≤ 100 인 정수
1 ≤ Ai ≤ Bi ≤ N

풀이
구간합의 문제여서 구간합으로 풀었음
시간복잡도 O(N+K)
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
scores = list(map(int, input().split()))

acc = [0] * (N+1)
sumation = 0
for i in range(N):
    sumation += scores[i]
    acc[i+1] = sumation
for i in range(K):
    A, B = map(int, input().split())
    length = B-A+1
    ans = (acc[B] - acc[A-1]) / length
    print(f'{ans:.2f}')