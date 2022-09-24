'''
row는 입력되는 대로 x를 기준으로 잘라서 길이를 비교해 숫자를 셌고
column은 임의로 2중 for문을 이용해 트랜스포즈 한 뒤에 row와 같은 방법으로 셌음
'''
N = int(input())

room = [input() for _ in range(N)]

row_space = 0
for row in room:
    spaces = list(row.split('X'))
    for space in spaces:
        if len(space) >= 2: row_space += 1

column_space = 0        
for i in range(N):
    column = ''
    for j in range(N):
        column += room[j][i]
    spaces = list(column.split('X'))
    for space in spaces:
        if len(space) >= 2: column_space += 1
print(row_space, column_space)
    