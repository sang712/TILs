'''
N의 최대 크기가 1000까지여서 그냥 2번 순회해도 되겠다 싶어 생각나는 대로 풀이하였음

처음 풀었을 때에는 A의 크기만 비교하고 뒤의 A가 더 크다면 max로 값을 갱신해주는 방식으로 진행하였는데
164ms가 걸려서 더 나은 속도를 가진 코드를 검색하였음

역시 dp 답게 0으로 초기화를 한 뒤, 방문을 마쳤을 때 +1을 해주고
연속 값의 크기비교는 if문에서 진행하는 방식이었음
104ms로 줄일 수 있었음 다만 천편일률적 코드
'''
N = int(input())
A = list(map(int, input().split()))
# dp = [1] * N
dp = [0] * N
for i in range(N):
    for j in range(i):
        if A[j] < A[i] and dp[j] > dp[i]:
            # dp[i] = max(dp[j] + 1, dp[i])
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))