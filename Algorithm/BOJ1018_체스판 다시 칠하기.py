N, M = map(int, input().split())
board = [input() for _ in range(N)]

ans_B = 2501
ans_W = 2501
B = "BWBWBWBW"
W = "WBWBWBWB"
for i in range(N-7):
    for j in range(M-7):
        to_B, to_W = 0, 0
        for k in range(8):
            for l, grid in enumerate(board[i+k][j:j+8]):
                if grid == B[l]:
                    if k % 2 == 0:
                        to_B += 1
                    else:
                        to_W += 1
                else:
                    if k % 2 == 0:
                        to_W += 1
                    else:
                        to_B += 1
        ans_B = min(ans_B, to_B)
        ans_W = min(ans_W, to_W)
print(min(ans_B, ans_W))