"""
요세푸스 순열을 구하는 문제 boj1158를 응용하여 풀이하였음

제외된 사람을 세는 cnt 변수와 방향을 바꾸는 dir 변수를 추가하였고
M회 제외할 때마다 dir변수를 1또는 -1로 바꾸었음
이전 문제에서는 사람의 수와는 다르게 0부터 시작하는 인덱스를 맞추기 위해 -1을 해주었었는데
방향이 거꾸로 되는 경우 -1이 필요가 없어져서
해당 부분을 max(dir, 0)을 통해 정방향일 때 -1, 역방향일 때 -0이 되도록 하였음
"""
N, K, M = map(int, input().split())
people = list(range(1, N+1))

ans = []
idx = 0
dir = 1
cnt = 0
for _ in range(N):
    idx = (idx + dir*K - max(dir, 0)) % len(people)
    ans.append(people.pop(idx))
    cnt += 1
    if cnt >= M:
        cnt = 0
        dir *= -1
print(*ans, sep='\n')
