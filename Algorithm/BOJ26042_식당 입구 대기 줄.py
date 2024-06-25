"""
입력이 10만개가 되어 pop(0)으로 하면 시간초과가 날 것 같아서
deque를 import해서 사용하였음
그 외에는 문제에서 요구한 대로 구현하였음
"""
import sys
import collections

input = sys.stdin.readline

line = collections.deque()
N = int(input())
length = 0
ans = [(0, 0)]
for _ in range(N):
    type_, *num = map(int, input().split())
    if type_ == 1:
        line.append(*num)
        length += 1
        if ans[0][0] < length:
            ans = [(length, line[-1])]
        elif ans[0][0] == length:
            ans.append((length, line[-1]))
    else:
        line.popleft()
        length -= 1
print(*sorted(ans)[0])