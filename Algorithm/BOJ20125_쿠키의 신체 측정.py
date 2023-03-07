"""
구현 문제로 문제에서 요구하는 대로 구현하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
board = []
heart = 0
for i in range(N):
    row = input()
    board.append(row)
    if not heart:
        for j in range(N):
            if row[j] == '*':
                heart = (i + 1, j)

left_arm = 0
for j in range(heart[1] - 1, -1, -1):
    if board[heart[0]][j] == '_':
        break
    left_arm += 1
    
right_arm = 0
for j in range(heart[1] + 1, N):
    if board[heart[0]][j] == '_':
        break
    right_arm += 1

waist = 0
for i in range(heart[0] + 1, N):
    if board[i][heart[1]] == '_':
        break
    waist += 1

left_leg = 0
for i in range(heart[0] + waist + 1, N):
    if board[i][heart[1] - 1] == '_':
        break
    left_leg += 1

right_leg = 0
for i in range(heart[0] + waist + 1, N):
    if board[i][heart[1] + 1] == '_':
        break
    right_leg += 1

print(*map(lambda x: x + 1, heart))
print(left_arm, right_arm, waist, left_leg, right_leg)