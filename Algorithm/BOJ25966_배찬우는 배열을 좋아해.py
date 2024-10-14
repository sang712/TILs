"""
문제가 요구하는 대로 구현하였고 시간 단축을 위해 출력을 한 번에 하도록 했음
"""
import sys
input = sys.stdin.readline

N, M, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for _ in range(q):
    query, *rest = map(int, input().split())
    if query:
        i, j = rest
        arr[i], arr[j] = arr[j], arr[i]
    else:
        i, j, k = rest
        arr[i][j] = k
ans = []
for row in arr:
    ans.append(' '.join(map(str, row)))
print(*ans, sep='\n')
