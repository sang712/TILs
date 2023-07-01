"""
파이썬의 zip() 함수와 언패킹 연산(?)인 *를 이용하면
2차원 리스트의 행과 열을 쉽게 바꿀 수 있다는 것을 이용해 풀이 하였음

단 세로로 되어있는 사탕은 'vo^'를 찾도록 해야함
"""
import sys
input = sys.stdin.readline

for t in range(int(input())):
    _ = input()
    
    r, c = map(int, input().split())
    box = [input() for _ in range(r)]
    
    cnt = 0
    for row in box:
        cnt += row.count('>o<')
        
    for row in zip(*box):
        cnt += ''.join(row).count('vo^')
            
    print(cnt)