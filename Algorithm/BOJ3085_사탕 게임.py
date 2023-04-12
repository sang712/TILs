"""
구현 문제로 문제에서 요구한대로
사탕 두개를 바꾼뒤 가장 길게 연속된 사탕의 수를 카운트하여 출력하도록 하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
board = [list(input()) for _ in range(N)]

def count_candies_row():
    max_candies = 0
    for i in range(N):
        Cs, Ps, Zs, Ys = 0, 0, 0, 0
        for j in range(N):
            serial_candy = 0
            if board[i][j] == 'C':
                Cs += 1
                serial_candy = Cs
                Ps, Zs, Ys = 0, 0, 0
            elif board[i][j] == 'P':
                Ps += 1
                serial_candy = Ps
                Cs, Zs, Ys = 0, 0, 0
            elif board[i][j] == 'Z':
                Zs += 1
                serial_candy = Zs
                Cs, Ps, Ys = 0, 0, 0
            elif board[i][j] == 'Y':
                Ys += 1
                serial_candy = Ys
                Cs, Ps, Zs = 0, 0, 0
            if max_candies < serial_candy:
                max_candies = serial_candy
    return max_candies

def count_candies_col():
    max_candies = 0
    for j in range(N):
        Cs, Ps, Zs, Ys = 0, 0, 0, 0
        for i in range(N):
            serial_candy = 0
            if board[i][j] == 'C':
                Cs += 1
                serial_candy = Cs
                Ps, Zs, Ys = 0, 0, 0
            elif board[i][j] == 'P':
                Ps += 1
                serial_candy = Ps
                Cs, Zs, Ys = 0, 0, 0
            elif board[i][j] == 'Z':
                Zs += 1
                serial_candy = Zs
                Cs, Ps, Ys = 0, 0, 0
            elif board[i][j] == 'Y':
                Ys += 1
                serial_candy = Ys
                Cs, Ps, Zs = 0, 0, 0
            if max_candies < serial_candy:
                max_candies = serial_candy
    return max_candies

answer = 0
for i in range(N):
    for j in range(N):
        if i < N - 1:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            temp_max = max(count_candies_col(), count_candies_row())
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            answer = max(temp_max, answer)
            
        if j < N - 1:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            temp_max = max(count_candies_col(), count_candies_row())
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            answer = max(temp_max, answer)
        if answer == N: break
    if answer == N: break
print(answer)
            