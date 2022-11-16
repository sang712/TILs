'''
이분탐색으로 구현하였음
2800ms대 소요
'''
N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = 2000000000

def cut(height):
    cnt = 0
    for tree in trees:
        cnt += tree - height if tree > height else 0
    return cnt

while start <= end:
    mid = (start + end)//2
    if cut(mid) < M:
        end = mid - 1
    else:
        start = mid + 1
print(end)


#400ms대 풀이
# Counter를 사용하였음
'''
import sys
from collections import Counter
n,m = map(int, sys.stdin.readline().split())
t = Counter(map(int, sys.stdin.read().split()))

s = 1
e = max(t.items())[0]

while s<=e:
    mid = (s+e)//2
    tot = sum((h-mid)*i for h,i in t.items() if h>mid)

    if tot >= m:
        s = mid+1
    elif tot <m:
        # ans = mid
        e = mid-1

print(e)
'''