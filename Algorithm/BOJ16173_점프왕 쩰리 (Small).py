"""
제한 조건으로 N이 3보다 같거나 작기 때문에 크기가 크지 않아서
방문처리를 따로 하지않았음

다만 고려했어야 하는 부분이 점프 거리가 0인 공간도 있어서 해당 부분에 도달할 경우
다음 지점으로 넘어갈 수 없다는 처리를 해줘야 한다는 점임
"""
N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

delta = [(0, 1), (1, 0)]
stack = [(0, 0)]
while stack:
    r, c = stack.pop()
    dist = board[r][c]
    if dist == -1:
        print('HaruHaru')
        break
    
    if dist == 0:
        continue
    
    for dr, dc in delta:
        nr, nc = r + dist * dr, c + dist * dc
        if 0 <= nr < N and 0 <= nc < N:
            stack.append((nr, nc))
else:
    print('Hing')