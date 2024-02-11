"""
우선 접근 방식은 다음과 같음
삼각형을 구성할 대포알의 개수를 구하고
그 값들을 이용해 사면체를 만들 때 필요한 대포알의 개수를 구했음
사면체에 사용된 대포알의 개수가 300,000개 이하가 되려면 삼각형은 120번까지만 구하면 되었음

그 후에 몇개를 사용하면 되는가를 구하는 문제가 남았는데 생각해보니 브루트포스가 아니라
조합별로 최선이 달라질 것이라는 생각이 들었음 그래서 dp로 풀이하였음 

pypy3로 212ms pypy3 중에서도 순위권이었는데
python3로 4900ms로 1600ms대 나오는 사람들과는 달리 조금 시간이 오래걸렸음

사면체를 구하기 위해 list를 두개를 만든 것을 하나로 압축했는데 500ms만 단축되었음
pypy3는 4ms 단축되었음

+) BFS로 풀면 더 빠르다 1600ms대가 BFS로 풀이한 것이었음
pypy3로 제출하면 남의코드로 1등할까봐 그냥 제출 안 했음
"""
N = int(input())

tetrahedron = []
triangle, temp = 0, 0
for n in range(1, 121):
    triangle += n
    temp += triangle
    if temp > N:
        break
    tetrahedron.append(temp)
    
dp = [10] * (N+1)
for i, n in enumerate(tetrahedron):
    if n <= N:
        dp[n] = 1
    else:
        break
for i in range(1, N+1):
    for j in tetrahedron:
        if j >= i:
            break
        if dp[i-j] + 1 < dp[i]:
            dp[i] = dp[i-j] + 1
print(dp[N])

"""
# BFS 풀이
import collections

def bfs():
    q = collections.deque()
    q.append((N, 0))

    visited = [0] * (N+1)
    visited[N] = 1

    while q:
        cannonballs, cnt = q.popleft()
        if cannonballs == 0:
            return cnt

        for n in tetrahedron:
            if n > cannonballs:
                continue

            nxt = cannonballs - n
            if visited[nxt]:
                continue

            visited[nxt] = 1
            q.append((nxt, cnt+1))

N = int(input())

tetrahedron = []
triangle, temp = 0, 0
for n in range(1, 121):
    triangle += n
    temp += triangle
    if temp > N:
        break
    tetrahedron.append(temp)

print(bfs())
"""