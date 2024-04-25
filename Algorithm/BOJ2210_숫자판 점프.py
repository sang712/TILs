"""
보드의 사이즈가 작아서 최악의 경우더라도 25 * 4 ^ 6 = 약 10만 이어서
그냥 dfs 방식으로 구현하였음
"""
board = [input().split() for _ in range(5)]

def make_num(sequence, r, c):
    if len(sequence) >= 6:
        nums.add(''.join(sequence))
        return
    
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            sequence.append(board[r][c])
            make_num(sequence, nr, nc)
            sequence.pop()
            
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
nums = set()
for i in range(5):
    for j in range(5):
        make_num([], i , j)
print(len(nums))