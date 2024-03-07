"""
그냥 popleft하고 append 해도 O(nk)라고 해서 그렇게 풀었는데 2112ms가 나와서 조금 어리둥절 했음
다른 풀이 보니까 pop, append를 여러번하지 않고 그냥 해당 부분을 pop(idx)로 가져오는 방식으로 풀이했음
알고리즘을 오래 풀면서 pop() 외에는 전혀 쓰지않던 pop(n)이었는데 이 문제를 풀 때는 써도 되는구나 싶었음
아마 이렇게 푸는게 진정한 O(nk)인 것 같음
"""
N, K = map(int, input().split())
q = list(range(1, N+1))

ans = []
idx = 0
for _ in range(N):
    idx = (idx + K - 1) % len(q)
    ans.append(q.pop(idx))
print('<', end='')
print(*ans, sep=', ', end='')
print('>')