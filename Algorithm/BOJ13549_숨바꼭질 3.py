'''
BOJ1697 숨바꼭질 문제와 비슷한 방식으로 풀었는데 이 방식이 BFS 방식이라는 걸 이 문제를 풀면서 알게 되었음

이동할 때의 가중치가 1과 0이라 다익스트라 방식을 적용할 수 있다는 점과
경우에 따라 가중치가 0과 1로 다를 경우 0-1 너비 우선 탐색 알고리즘을 적용할 수 있다는 점을 알게 되었음
가중치에 상관없이 그냥 append하였을 때는 728ms가 소요되었는데
가중치가 낮을 때에 우선을 두고 appendleft를 하였을 때는 236ms가 소요되었음

100ms대도 확인해봤는데 K가 N보다 작을 때는 그냥 빼기를 하는 것으로 시간을 단축한 것 같았음
시도한 결과 236ms에서 192ms 로 44ms 정도 단축할 수 있었음
해당 코드는 BFS 구문을 함수형태로 만들어 K가 N보다 작을 때는 함수를 호출하지 않는 것으로 했는데
나는 while문으로 작성했기 때문에 그냥 경우를 추가하여서 시간 단축이 그리 많이 되지 않은 것 같음
'''
from collections import deque

N, K = map(int, input().split())

visited = [0] * 100001
time = [100001] * 100001
q = deque()
if K <= N:
    q.append((K, N-K))
    time[K] = N-K
else:
    q.append((N, 0))
    time[N] = 0

while q:
    cur_pos, t = q.popleft()
    visited[cur_pos] = 1
    
    if cur_pos == K:
        break
    
    for move, t in [(-1, 1), (1,  1), (cur_pos, 0)]:
        next_pos = cur_pos + move
        if 0 <= next_pos < 100001 and not visited[next_pos]:
            time[next_pos] = min(time[next_pos], time[cur_pos] + t)
            if t:
                q.append((next_pos, t))
            else:
                q.appendleft((next_pos, t))
print(time[K])