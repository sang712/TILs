"""
?를 찾아서 앞의 단어의 마지막 글자, 뒤의 단어의 첫 글자를 저장한 뒤
해당 글자로 시작하고 끝나는 단어이면서 끝말잇기에 사용되지 않은 단어를 찾아 출력하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
S = [input().strip() for _ in range(N)]
M = int(input())
A = [input().strip() for _ in range(M)]

start, end = '', ''
for i in range(N):
    if S[i] == '?':
        if i > 0:
            start = S[i-1][-1]
        if i < N - 1:
            end = S[i+1][0]

s_set = set(S)
for a in A:
    if a.startswith(start) and a.endswith(end) and a not in s_set:
        print(a)
        break