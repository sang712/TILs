'''
처음에 고려할 때 50001 100000과 같은 극값에서 순간이동을 한 뒤에 이동을 한 경우도 고려하기 위해
list의 범위를 200001까지로 잡았는데
2가 곱해진 뒤에 뒤로 돌아가려면 2배의 시간을 소요하므로 고려할 필요조차 없었음
해당 결과로 320ms에서 192ms로 시간을 단축할 수 있었음
'''
from collections import deque

N, K = map(int, input().split())

dq = deque()
dq.append((N, 0))

visited = [0] * 100001

while dq:
    cur_pos, cnt = dq.popleft()
    if cur_pos > 100000:
        continue
    if visited[cur_pos]:
        continue
    else:
        visited[cur_pos] = 1
    if K == cur_pos:
        print(cnt)
        break
    dq.append((cur_pos * 2, cnt + 1))
    dq.append((cur_pos + 1, cnt + 1))
    if cur_pos > 0:
        dq.append((cur_pos - 1, cnt + 1))