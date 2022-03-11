'''
1) 파이썬 내장함수를 사용하기
replace() 함수를 이용해 'XXXX'와 'XX'를 찾아 바꾸고
find() 함수를 통해 'X'가 남아있는지 확인하여 결과를 출력함

2) 직접 알고리즘을 짜서 풀기
while문으로 입력값의 idx로 접근하면서 
.이 나오거나 끝이 될 때까지 이어진 X의 개수를 파악하고
이어진 X를 4개씩 2개씩 나누면서 새로운 출력에 더하고
X가 홀수개로 남으면 -1을 반환함
.이 나오면 출력값에 .을 더함
'''
board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')
if board.find('X') >= 0:
    print('-1')
else:
    print(board)
