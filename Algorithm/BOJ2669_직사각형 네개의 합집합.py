"""
주어진 제한조건이 작기 때문에 일일이 세는 방식으로 구현하였음
반복문으로 입력된 좌표 사이를 돌면서
처음 방문하는 곳이면 카운팅을 하는 방식으로 풀이함
"""
board = [[0] * 101 for _ in range(101)]

area = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            if board[x][y] == 0:
                area += 1
                board[x][y] = 1
print(area)