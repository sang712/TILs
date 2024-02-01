"""
그냥 풀면 되는 문제인 줄 알았더니 문제를 제대로 안 읽어서
마지막 예시에 돌에 적혀있는 숫자의 배수만큼 뛸 수 있다는 것을 나중에 알았고
그걸로도 모자라 왼쪽으로도 점프가 되는 걸 다시 알게 되어 푸는데 시간이 오래걸렸음
돌아돌아 BFS로 풀이하였고 시간을 단축하기 위해 방문체크를 하는 visited를 추가하였음
그래도 다른 사람들처럼 70ms대는 안 나오고 120ms가 나오더라
"""
import collections

N = int(input())
stones = [0] + list(map(int, input().split()))
a, b = map(int, input().split())
visited = [0] * (N+1)

q = collections.deque()
q.append((a, 0))

while q:
    pos, jumps = q.popleft()
    if pos == b:
        print(jumps)
        break
    if visited[pos]:
        continue
    visited[pos] = 1
    jump = stones[pos]
    for i in range(jump, N, jump):
        if pos+i > N:
            break
        q.append((pos+i, jumps+1))
    for i in range(jump, N, jump):
        if pos-i <= 0:
            break
        q.append((pos-i, jumps+1))
else:
    print(-1)