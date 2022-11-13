'''
이분 탐색을 이용한 풀이
'''
import sys
input = sys.stdin.readline
K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))

start = 1
end = max(lines)

while start <= end:
    mid = (start+end) // 2

    cnt = 0
    for line in lines:
        cnt += line // mid

    if cnt >= N:
        start = mid+1
    else:
        end = mid-1

print(end)
    
