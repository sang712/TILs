"""
문제에서 요구하는 대로 구현하였고
Z를 A로 바꾸는 부분은 ord로 ASCII코드로 변환한다음 64를 빼서 
알파벳 순서를 다음으로 변경함에 있어 코드 번호의 영향이 없게 만들고
26으로 %연산을 해 Z가 A로 넘어가는 부분을 처리한 후에 다시 65를 더하고
chr함수로 문자열로 변환하였음
"""
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
S = list(input().strip())
ans = []
for _ in range(Q):
    q, l, r = map(int, input().split())
    if q == 1:
        cnt = 1
        p = S[l-1]
        for i in range(l, r):
            if S[i] != p:
                cnt += 1
            p = S[i]
        ans.append(cnt)
    elif q == 2:
        for i in range(l-1, r):
            S[i] = chr((ord(S[i])-64)%26+65)
print(*ans, sep='\n')
