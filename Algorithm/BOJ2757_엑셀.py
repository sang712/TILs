"""
열의 숫자를 26으로 나누면서 해당 수를 문자로 바꾸는 방식을 이용해 풀이하였음
"""
import sys
input = sys.stdin.readline

ans = []
while True:
    rc = input().strip()[1:]
    r, c = rc.split('C')
    if r == c == '0':
        break
    cell_name = []
    c = int(c) - 1
    while c >= 26:
        col = c % 26
        cell_name.append(chr(ord('A') + col))
        c = c // 26 - 1
    cell_name.append(chr(ord('A') + c))
    cell_name.reverse()
    cell_name.append(r)
    ans.append(''.join(cell_name))
    
print(*ans, sep='\n')