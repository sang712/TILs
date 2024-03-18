"""
각 자리수에 해당하는 수가 결과에 도달하기까지 몇 번 더해지는지 보면
n-1Ci 번 더해짐
그래서 컴비네이션 구하고 순열 만들어서 일일이 대입해 계산한 뒤 결과를 출력하였음
더 빨리 구하는 방법이 있는 것 같은데 공개된 답이 아니라 확인하진 못 했음
"""
N, F = map(int, input().split())
comb = [1] * N
for i in range(N-1):
    if i > N // 2:
        comb[i] = comb[N-1-i]
    else:
        temp = 1
        for k in range(N-1, N-1-i, -1):
            temp *= k
        for k in range(2, i+1):
            temp //= k
        comb[i] = temp
visited = [0] * (N+1)
perm = []
ans = []
def permuation(order, sumation):
    if order == N and sumation == F:
        ans.append(tuple(perm))
        return
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = 1
        perm.append(i)
        permuation(order+1, sumation + i*comb[order])
        visited[i] = 0
        perm.pop()
permuation(0, 0)
print(*ans[0])