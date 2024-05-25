"""
행렬곱을 진행해서 각 곱의 두 항이 모두 1이면 중단하고 카운팅을 한 뒤
다음 원소를 계산하도록 하였음
"""
import sys


input = sys.stdin.readline
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        for m in range(N):
            if A[i][m] == B[m][j] == 1:
                ans += 1
                break
print(ans)