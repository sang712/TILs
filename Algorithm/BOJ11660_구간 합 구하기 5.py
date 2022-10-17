'''
행렬을 더하고 빼는 과정에서 0으로 된 더미 행, 열이 있으면 좋을 것 같아서 
dp를 N+1*N+1 크기로 설정하였음
누적합 행렬을 만드는 것은 어렵지 않았지만
(전 행, 전 열, 현재 값을 모두 더하고 전 행열 값을 빼는 방법)
누적합 행렬을 사용하는 것에 있어 고민이 필요하였다
결론적으로 누적합을 이용해 기존 행렬의 구역의 합을 구하려면
구하려는 구역의 최대 누적합에서 구역을 제외한 행의 누적합, 열의 누적합을 빼고,
그 행과 열의 교집합을 더해주면 된다.
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (N+1) for _ in range(N+1)]

dp[1][1] = table[0][0]
for i in range(1, N+1):
    for j in range(1, N+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + table[i-1][j-1] - dp[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])