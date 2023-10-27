"""
동전을 뒤집을 때마다 굳이 나머지 동전 또한 뒤집을 필요 없이
각 위치별로 뒤집은 횟수를 누적하여 계속해서 더해나가는 방식으로 구현하였음
그리고 뒤집은 횟수와 동전의 초기 상태를 더해서 홀수면 뒤집고, 아니면 그대로 두었음
"""

N, M = map(int, input().split())

coins = [list(map(int, list(input()))) for _ in range(N)]
flip_counter = [[0] * M for _ in range(N)]
delta = [(-1, 0), (-1, -1), (0, -1)]
cnt = 0
for i in range(N - 1, -1, -1):
    for j in range(M - 1, -1, -1):
        if (flip_counter[i][j] + coins[i][j]) % 2:
            cnt += 1
            flip_counter[i][j] += 1
        for di, dj in delta:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                flip_counter[ni][nj] += flip_counter[i][j]
print(cnt)