'''
pop과 append가 빈번하게 일어나는 문제라 deque를 사용하였음
홀수는 첫번째 순회에서 모두 사라지기 때문에 시간을 줄이기 위해 처음에 제외하였음

260ms초가 걸렸는데 60ms대의 사람들이 있어서 확인해 보았더니 규칙이 있었음
1 2 2 4 2 4 6 8 2 4 6 8 10 12 14 16
과 같이 2곱하기 2의 제곱수에 해당하는 수까지 반복되는 규칙이 발견됨
해당 규칙으로 구현하면 60ms대의 결과를 얻을 수 있음
'''
from collections import deque

N = int(input())

dq = deque([i*2 for i in range(1, (N//2)+1)])

DISCARD, TOBACK = -1, 1
switch = TOBACK if N%2 else DISCARD
while len(dq) > 1:
    if switch == DISCARD:
        dq.popleft()
    elif switch == TOBACK:
        dq.append(dq.popleft())
    switch *= -1

ans = dq.popleft() if N > 1 else 1
print(ans)