"""
하얀 칸의 좌표 값 x, y의 합이 짝수라는 점을 이용해 풀이하였음
"""
board = [input() for _ in range(8)]
ans = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2:
            continue
        if board[i][j] == 'F':
            ans += 1
print(ans)