'''
시간 초과를 피하려고 출력 결과를 ans = '' 저장하려고 했더니 메모리 초과가 나서
해당 일 때 print()로 바꾸는 것으로 수정하였음
'''
import sys
input = sys.stdin.readline

M = int(input())
S = []
# ans = ''
for i in range(M):
    command = input().split()
    order = command[0]
    if len(command) == 1:
        if order == 'all':
            S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        elif order == 'empty':
            S = []
    else:
        num = int(command[1])
        if order == 'add':
            if not num in S:
                S.append(num)
        elif order == 'remove':
            if num in S:
                S.pop(S.index(num))
        elif order == 'check':
            if num in S:
                # ans += '1\n'
                print(1)
            else:
                # ans += '0\n'
                print(0)
        elif order == 'toggle':
            if num in S:
                S.pop(S.index(num))
            else:
                S.append(num)
# print(ans, end='')