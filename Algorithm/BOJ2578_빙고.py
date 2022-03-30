'''
딕셔너리로 번호와 위치를 연관 짓고
불리는 번호를 딕셔너리의 키로 넣어 값을 꺼내 사용
라인에서 마크된 숫자의 개수가 5개가 되면 카운트 하고
3개 이상이면 중간에 return으로 중단
'''
board = {}
i = 0
for _ in range(5):
  row = map(int, input().split())
  for num in row:
    board.setdefault(num, i)
    i += 1

rows = [0, 0, 0, 0, 0]
cols = [0 ,0, 0, 0, 0]
diagonals = [0, 0]

def mark(num):
  pos = board[num]
  rows[int(pos/5)] += 1
  cols[int(pos%5)] += 1
  if pos in [12]:
    diagonals[0] += 1
    diagonals[1] += 1
  elif pos in [0, 6, 12, 18, 24]:
    diagonals[0] += 1
  elif pos in [4, 8, 12, 16, 20]:
    diagonals[1] += 1

def solve():
  k = 1
  order = [list(map(int, input().split())) for _ in range(5)]
  for i in range(5):
    for j in range(5):
      mark(order[i][j])
      if k >= 12:
        if rows.count(5) + cols.count(5) + diagonals.count(5) >= 3:
          return print(k)
      k += 1
solve()
