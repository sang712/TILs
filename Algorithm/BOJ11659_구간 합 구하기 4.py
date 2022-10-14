'''
input의 line 수가 100000이므로 readline을 사용하였고
dp를 이용하여 누적합 리스트를 만들었음
dp[k+1] += dp[k] + nums[k] 로 작성하여서 304ms 였던 거 + 기호 빼서 268초로 단축하였음
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split()))

dp = [0] * (N+1)

for k in range(N):
    dp[k+1] = dp[k] + nums[k]

for _ in range(M):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])