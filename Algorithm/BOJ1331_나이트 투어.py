"""
입력을 받아서 이동한 순서대로 각 행과 열의 차이를 계산하여 
둘의 곱이 2인 경우를 만족하지 않거나,
첫 입력과 마지막입력이 위의 조건을 만족하지 않거나,
입력을 받은 경로를 집합으로 변환했을 때 원소의 개수가 36개가 아닌 경우
Invalid를 출력하였음
위의 조건을 모두 만족하는 경우 Valid를 출력하도록 하였음

추가로 중간에 루프 중에 입력을 받도록 했었는데
조건을 만족하지 않으면 입력을 모두 받지 못하고 루프를 빠져나오게 되어 에러가 발생했음
처음에 입력을 다 받도록 수정하였음
"""
alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}

trajectory = [input() for _ in range(36)]
for i in range(1, 36):
    l_col, l_row = trajectory[i-1]
    c_col, c_row = trajectory[i]
    gap_col = abs(alphabet[c_col] - alphabet[l_col])
    gap_row = abs(int(c_row) - int(l_row))
    if not gap_row * gap_col == 2:
        print('Invalid')
        break
else:
    l_col, l_row = trajectory[-1]
    c_col, c_row = trajectory[0]
    gap_col = abs(alphabet[c_col] - alphabet[l_col])
    gap_row = abs(int(c_row) - int(l_row))
    if not gap_row * gap_col == 2 or not len(set(trajectory)) == 36:
        print('Invalid')
    else:
        print('Valid')