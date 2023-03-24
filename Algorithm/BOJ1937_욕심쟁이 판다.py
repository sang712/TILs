"""
어제 풀었던 문제와는 다르게
시작점과 끝점이 따로 주어지지 않았다는 점이 다름

그래서 dp에는 해당 시작점에서 시작했을 때 갈 수 있는 가장 먼 거리를 담아야할 것 같음
dfs에서 크기 방향을 다르게 잡으면 해당 점을 도착점으로 할 때의 가장 먼 거리를 담을 수 있음

시작점과 끝점이 따로 없기 때문에 2중 for문으로 dfs를 호출하도록 하였고
해당 과정에서 max값을 얻도록 하였음

어제의 문제와 또 다른 점 하나는 어제 문제는 -1을 dp의 초기화 값으로 사용하였는데
이번 문제는 칸에 접근 하는 것 만으로도 1로 갱신되기 때문에 
-1로 초기화하지 않고 0으로 초기화해도 무방하였음
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1_000_000)

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(r: int, c: int) -> int:
    if dp[r][c] > 0:
        return dp[r][c]
    
    ways = [0]
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and forest[r][c] < forest[nr][nc]:
            ways.append(dfs(nr, nc))
    
    dp[r][c] = max(ways) + 1
    return dp[r][c]

possible_num = set()
for i in range(N):
    for j in range(N):
        if not dp[i][j]:
            possible_num.add(dfs(i, j))
print(max(possible_num))