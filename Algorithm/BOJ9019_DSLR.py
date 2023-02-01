"""
처음에 문제에서 요구하는대로 구현하였는데 python3에서는 시간초과가 났고
pypy3에서는 19500ms 라는 처음 보는 시간이 소요되었음 
문자열을 더하는 등의 처리하는 과정에서 시간을 많이 소요한다고 하여
문자열로 변환하지 않고 숫자로 연산을 하는 방법으로 구현하였더니
6320ms로 줄일 수 있었고
여기에 input을 readline으로 바꾸어 4800ms로 줄일 수 있었음
그런데 어느하나 python으로 통과되는 것이 없어서 답을 찾아보았는데
양쪽에서 출발해서 만나면 그 값으로 결정하는 방식을 취하는 듯 해 보였음
"""
import sys
from collections import deque

input = sys.stdin.readline

def dslr_bfs(from_this: int, to_this: int) -> str:
    visited = [0] * 10001
    roots = [-1] * 10001
    commands = [''] * 10001
    
    q = deque()
    q.append(from_this)
    while q:
        before = q.popleft()
        if before == to_this:
            break
        
        if visited[before]:
            continue
        visited[before] = 1
        
        D = (before * 2) % 10000
        if roots[D] == -1:
            q.append(D)
            roots[D] = before
            commands[D] = 'D'
        
        S = (before - 1) % 10000
        if roots[S] == -1:
            q.append(S)
            roots[S] = before
            commands[S] = 'S'
        
        L = (before * 10) % 10000 + before // 1000
        if roots[L] == -1:
            q.append(L)
            roots[L] = before
            commands[L] = 'L'
        
        R = before // 10 + (before % 10) * 1000
        if roots[R] == -1:
            q.append(R)
            roots[R] = before
            commands[R] = 'R'
        
    command = deque()
    while commands[to_this] and to_this != from_this:
        command.appendleft(commands[to_this])
        to_this = roots[to_this]
        
    return ''.join(command)
        
for tc in range(int(input())):
    A, B = map(int, input().split())    
    print(dslr_bfs(A, B))

# 파이썬 통과 코드    
"""
import sys
from collections import deque
input = sys.stdin.readline

T = int(input().rstrip())
C = ['D', 'S', 'L', 'R', 'D']

for _ in range(T):
    ans = ''
    dp = [-1] * 10000
    dp2 = [-1] * 10000
    A, B = map(int, input().rstrip().split(' '))
    dp[A] = ''
    dp2[B] = ''
    q = deque([(A, 1), (B, 2)])
    while q:
        #출발점 뻗어 나가기
        a, t = q.popleft()
        if t == 1:
            for i in range(4):
                if C[i] == 'D':
                    tf = (a * 2) % 10000
                elif C[i] == 'S':
                    tf = 9999 if a == 0 else a - 1
                elif C[i] == 'L':
                    temp = '0' * (4 - len(str(a))) + str(a)
                    tf = int(temp[1:] + temp[0])
                elif C[i] == 'R':
                    temp = '0' * (4 - len(str(a))) + str(a)
                    tf = int(temp[-1] + temp[:-1])

                if dp2[tf] != -1:
                    ans = dp[a] + C[i] + dp2[tf]
                    break

                if dp[tf] == -1 or len(dp[tf]) > (len(dp[a]) + 1):
                    dp[tf] = dp[a] + C[i]
                    q.append((tf, 1))

        # 도착점 반대로 뻗어나가기
        if t == 2:
            for i in range(5):
                if i == 0:
                    if a % 2:
                        continue
                    tf = (a // 2)
                elif i == 1:
                    tf = 0 if a == 9999 else a + 1
                elif i == 2:
                    temp = '0' * (4 - len(str(a))) + str(a)
                    tf = int(temp[-1] + temp[:-1])
                elif i == 3:
                    temp = '0' * (4 - len(str(a))) + str(a)
                    tf = int(temp[1:] + temp[0])
                elif i == 4:
                    if a % 2:
                        continue
                    tf = ((a + 10000) // 2)

                if dp[tf] != -1:
                    ans = dp[tf] + C[i] + dp2[a]
                    break

                if dp2[tf] == -1 or len(dp2[tf]) > (len(dp2[a]) + 1):
                    dp2[tf] = C[i] + dp2[a]
                    q.append((tf, 2))

        if ans:
            break

    print(ans)
"""