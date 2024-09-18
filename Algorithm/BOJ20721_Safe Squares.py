def count_safe_squares(board):
    # identify which hs rookie
    rows_with_rooks = set()
    cols_with_rooks = set()
    
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                rows_with_rooks.add(i)
                cols_with_rooks.add(j)
    
    # count sfe rookies
    safe_squares = 0
    for i in range(8):
        for j in range(8):
            #squre if no sfe rookie
            if board[i][j] == '.' and i not in rows_with_rooks and j not in cols_with_rooks:
                safe_squares += 1
    
    return safe_squares

board = [input().strip() for _ in range(8)]

# number sfe rookie
result = count_safe_squares(board)

print(result if result > 0 else 0)
