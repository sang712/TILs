# pypy3로 해야 시간초과가 안 남
import sys
input = sys.stdin.readline
N, K, M = map(int, input().rstrip().split())

kimbobs = []
max_P = -1
def binary_search(start, end):
    global max_P

    if start > end:
        print(max_P)
        return

    mid = (start + end) // 2

    sum = 0
    for k in kimbobs:
        sum += k // mid

    if sum >= M:
        max_P = max(mid, max_P)
        binary_search(mid + 1, end)
    else:
        binary_search(start, mid - 1)

for _ in range(N):
    L = int(input())

    if L > 2*K:
        kimbobs.append(L-2*K)
    elif 2*K > L > K:
        kimbobs.append(L-K)

if len(kimbobs) == 0:
    print(-1)
else:
    kimbobs.sort()
    binary_search(1, kimbobs[-1])
