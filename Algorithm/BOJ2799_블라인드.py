"""
문제에서 요구하는 사항을 구현하였음
"""
M, N = map(int, input().split())
windows = [input() for _ in range(5*M + 1)]
ans = [0] * 5
for i in range(M):
    for j in range(N):
        for k in range(4):
            if windows[5*i + 1 + k][5*j + 1] == '.':
                ans[k] += 1
                break
        else:
            ans[4] += 1
print(*ans)