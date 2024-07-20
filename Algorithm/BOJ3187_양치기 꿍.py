"""
이중 for문으로 모든 부분을 dfs 방식으로 돌면서 구역을 확인했고
해당 구역내에 양과 늑대의 마릿수를 세서 양이 많을 경우 양만을
그 외의 경우의는 늑대만을 계산하여 출력하였음
"""
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
field = [list(input().strip()) for _ in range(R)]

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def count_animals(r, c):
    q = [(r, c)]
    k = v = 0
    while q:
        r, c = q.pop()
        if field[r][c] == 'k':
            k += 1
        elif field[r][c] == 'v':
            v += 1
        field[r][c] = '#'
        
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and field[nr][nc] != '#':
                q.append((nr, nc))
    return k, v

ans = [0, 0]
for r in range(R):
    for c in range(C):
        if field[r][c] != '#':
            k, v = count_animals(r, c)
            if k > v:
                ans[0] += k
            else:
                ans[1] += v
print(*ans)