"""
입력을 받아서 그대로 출력하였음
끝을 확인하기 위해 try except 문을 사용하였음
"""
import sys
input = sys.stdin.readline

ans = []
try:
    for _ in range(100):
        ans.append(input())
except EOFError:
    pass
print(*ans, sep='')