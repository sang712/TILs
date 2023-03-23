"""
dfs 방식으로 일련의 과정을 따라가면서 나뉘는 분기를 저장하고
이미 도달한 적이 있다면 해당 값을 그대로 사용하도록 dp를 적용함
나뉜 분기가 이미 도달한 적이 있을 때 횟수를 카운팅하는 게 아니라
재귀를 타고 돌아왔을 때(분기를 탄 자리에서) 나뉜 분기를 합하는 방식임
그래서 시작점인 dp[0][0]이 답을 가짐
dp[i][j]가 갖는 의미는 점(i, j) 에서 부터 끝 점(M - 1, N - 1) 까지 갈 수 있는 경우의 수임

dp 없이 작성한 코드를 주피터 노트북으로 돌려봤는데 최악의 조건의 경우 걸리는 시간을 2시간이 지난 아직까지도 측정이 되고 있지 않음
주로 7회 반복되니까 해당 횟수로 고려하면 기존 코드는 최소 10분 이상 씩은 걸린다는 소리
그래서 문제 풀이를 보고 풀이를 작성하였음

문제를 풀면서 문제가 되었던 점은
dp의 기본 값을 -1이 아닌 0으로 잡았던 점인데 이렇게 되면 직전 값보다 작아서 해당 값에 도달했지만
주변 값이 모두 큰 경우 해당 좌표를 4번씩 더 돌게 되면서(해당 경우 dp의 의미가 사라짐) 시간초과가 났음
다시 말하면 해당 점에서 출발했을 때 도착할 수 있는 경우가 없는 경우를 0으로 저장해야 하기 때문에
기본 값을 -1로 저장했어야 했음

이렇게 오늘 배운 내용을 응용하기 위해 내일 같은 유형, 같은 난도의 문제인
BOJ1937 욕심쟁이 판다 문제를 풀도록 하겠음
"""
import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

dp = [[-1] * N for _ in range(M)]
dp[M - 1][N - 1] = 1

def dfs(r: int, c: int) -> int:
    if r == M - 1 and c == N - 1:
        return 1
    
    if dp[r][c] >= 0:
        return dp[r][c]
    
    cnt = 0
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < M and 0 <= nc < N and board[r][c] > board[nr][nc]:
            cnt += dfs(nr, nc)
            
    dp[r][c] = cnt
    return cnt

print(dfs(0, 0))