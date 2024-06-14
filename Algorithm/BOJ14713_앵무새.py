"""
앵무새가 한 말이 할 말과 모두 일치하지 않는 경우를 판단하지 않아서 틀렸었고
해당 부분을 추가하여 정답을 받았음
"""
import sys
input = sys.stdin.readline

N = int(input())
S = [input().split() for _ in range(N)]
L = input().split()

for l in L:
    for s in S:
        if s and s[0] == l:
            s.pop(0)
            break
    else:
        print('Impossible')
        break
else:
    for s in S:
        if s:
            print('Impossible')
            break
    else:
        print('Possible')