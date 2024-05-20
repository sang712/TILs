"""
오랜시간이 걸릴거라 생각해서 pypy3로 제출했었는데 그냥 python3로 풀어도 빠른시간에 풀리는 문제
문제에서 요구하는 대로 그대로 구현하여 풀이하였음
시작점 1부터 k씩 움직이며 장애물이 만나면 되돌아가고
도착점 Z를 만날 때 까지 계속 움직이도록 하였음
다만 첫 풀이에서 고려하지 않은 것이 방문처리를 하지 않으면 무한루프를 돌 수 있기 때문에
방문처리를 하여 해당 부분을 해결하였음
"""
N, Z, M = map(int, input().split())
obstacles = set(map(int, input().split()))

def run(k):
    pos = 1
    visited = set([1])
    while not pos == Z:
        pos = pos + k
        if pos > N:
            pos -= N
        if pos in visited:
            return False
        visited.add(pos)
        if pos in obstacles:
            return False
    return True

for i in range(1, N):
    if run(i):
        print(i)
        break