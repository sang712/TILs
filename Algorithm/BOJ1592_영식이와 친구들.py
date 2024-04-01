"""
주어진 제한 조건대로 구현하였음
"""
N, M, L = map(int, input().split())

cnt = 0
idx = 0
people = [1] + [0] * (N-1)
while people[idx] < M:
    cnt += 1
    if people[idx] % 2:
        idx = (idx+L) % N
    else:
        idx = (idx-L) % N
    people[idx] += 1
print(cnt)