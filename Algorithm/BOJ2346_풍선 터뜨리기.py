"""
그냥 list로 구현해서 방문한 곳은 0으로 만들고, 0을 만나면 while문으로 계속 움직이는 방식으로 했더니
0인 부분을 건너뛰게 되면 0인 부분을 칸으로 인정하고 움직인 것으로 판단해서 틀린답이 되는 것이었다.
deque로 그냥 문제를 풀어버렸다.
"""
import collections

N = int(input())
dq = collections.deque(enumerate(map(int, input().split())))

ans = []
while dq:
    idx, num = dq.popleft()
    ans.append(idx + 1)
    
    if num > 0:
        dq.rotate(-(num - 1))
    else:
        dq.rotate(-num)
print(*ans)
