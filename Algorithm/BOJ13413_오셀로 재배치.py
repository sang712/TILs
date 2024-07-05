"""
서로 매칭이 되는 경우와
각각 흰색인 말의 수를 세서 
말의 수의 차이와 매칭이 안 됐을 때 교환해야 되는 횟수를 세서
더한 뒤 출력하였음
"""
import sys
input = sys.stdin.readline

for t in range(int(input())):
    N = int(input())
    A = input()
    B = input()
    num_aw = num_bw = 0
    for i in range(N):
        a = A[i]
        b = B[i]
        if a != b:
            if a == 'W':
                num_aw += 1
            else:
                num_bw += 1
    ans = abs(num_aw-num_bw)
    ans += (num_aw + num_bw - ans)//2
    print(ans)