"""
2713번과 짝궁 문제로 해당문제와 비슷하게 풀이하였음
돌아가는 달팽이 문제는 방문처리하면서 탐색을 하는데
내부에 방향을 돌리는 4회 반복 for문을 추가해서 네 방향을 차례로 확인하고
그 방향으로 갈 수 있을 때를 확정하고 for문을 탈출하는 방식으로 구현하면 된다는 것을 숙지했음
"""
import sys
input = sys.stdin.readline

code = {'00000': ' ', '00001': 'A', '00010': 'B', '00011': 'C', '00100': 'D',
        '00101': 'E', '00110': 'F', '00111': 'G', '01000': 'H', '01001': 'I',
        '01010': 'J', '01011': 'K', '01100': 'L', '01101': 'M', '01110': 'N',
        '01111': 'O', '10000': 'P', '10001': 'Q', '10010': 'R', '10011': 'S',
        '10100': 'T', '10101': 'U', '10110': 'V', '10111': 'W', '11000': 'X',
        '11001': 'Y', '11010': 'Z'}

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ans = []
for t in range(int(input())):
    R, C, message = input().split()
    R = int(R)
    C = int(C)
    board = [list(message[r*C:(r+1)*C]) for r in range(R)]
    visited = [[0]*C for _ in range(R)]
    r, c = 0, 0
    i = 0
    text = []
    while True:
        text.append(board[r][c])
        visited[r][c] = 1
        
        for _ in range(4):
            dr, dc = delta[i]
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                r, c = nr, nc
                break
            i = (i+1) % 4
        else:
            break
    text = [''.join(code[''.join(text[i*5:(i+1)*5])]) for i in range(len(text)//5)]
    ans.append(''.join(text).rstrip())
print(*ans, sep='\n')