"""
N*N 2차원 리스트를 만들어서
중앙부터 숫자를 차례로 채우는 반복문을 만들었고
중간에 입력에서 요구하는 숫자를 만나면 좌표를 저장했다가 출력하도록 하였음
"""
N = int(input())
m = int(input())

snail = [[0] * N for _ in range(N)]

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

center = r = c = N // 2
snail[r][c] = 1
ans = (r + 1, c + 1)
cnt = 2
for scale in range(1, (N + 1) // 2):
    r = r - 1
    snail[r][c] = cnt
    if cnt == m:
        ans = (r + 1, c + 1)
    cnt += 1
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        low_limit = max(center - scale, 0)
        high_limit = min(center + scale, N - 1)
        while low_limit <= nr <= high_limit and low_limit <= nc <= high_limit:
            snail[nr][nc] = cnt
            r, c = nr, nc
            if cnt == m:
                ans = (r + 1, c + 1)
            cnt += 1
            nr, nc = r + dr, c + dc
for row in snail:
    print(*row)
print(*ans)