"""
주어진 메시지가 공백으로 시작하는 경우 split()으로 자르면 해당 부분이 제거되므로
이 부분에 유의하며 짜느라 시간이 오래 소요됨
"""
import sys
input = sys.stdin.readline

code = {' ': '00000', 'A': '00001', 'B': '00010', 'C': '00011', 'D': '00100',
        'E': '00101', 'F': '00110', 'G': '00111', 'H': '01000', 'I': '01001',
        'J': '01010', 'K': '01011', 'L': '01100', 'M': '01101', 'N': '01110',
        'O': '01111', 'P': '10000', 'Q': '10001', 'R': '10010', 'S': '10011',
        'T': '10100', 'U': '10101', 'V': '10110', 'W': '10111', 'X': '11000',
        'Y': '11001', 'Z': '11010'}
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for t in range(int(input())):
    raw = input()[:-1]
    R = int(raw[:2])
    raw = raw[2:].lstrip()
    C = int(raw[:2])
    raw = raw[2:]
    message = raw[1:] if C >= 10 else raw
    board = [['0']*C for _ in range(R)]
    visited = [[0]*C for _ in range(R)]
    message = ''.join([code[word] for word in message])
    r, c = 0, 0
    i = 0
    for char in message:
        if not visited[r][c]:
            visited[r][c] = 1
            board[r][c] = char
        else:
            i = (i + 1) % 4
            dr, dc = delta[i]
            r, c = r + dr, c + dc
            board[r][c] = char
            visited[r][c] = 1
        dr, dc = delta[i]
        nr, nc = r + dr, c + dc
        for _ in range(4):
            if not (0 <= nr < R and 0 <= nc < C and not visited[nr][nc]):
                i = (i + 1) % 4
                dr, dc = delta[i]
                nr, nc = r + dr, c + dc
            else:
                break
        r, c = nr, nc
    print(''.join(map(''.join, board)))