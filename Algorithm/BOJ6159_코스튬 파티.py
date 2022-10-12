'''
브루트포스로 구현하였음
두 포인터로 문제를 풀 수도 있다고 하여 해당 부분을 찾아봐야 할 것
'''
import sys
input = sys.stdin.readline
N, S = map(int, input().split())
cows = list()
for _ in range(N):
    cows.append(int(input()))

cnt = 0
for i in range(N-1):
    for j in range(i+1, N):
        if cows[i] + cows[j] <= S:
            cnt += 1
            
print(cnt)