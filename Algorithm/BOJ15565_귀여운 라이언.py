"""
투 포인터로 시작점과 끝점을 0과 K로 두고
구간 내에 K만큼의 1이 있으면 시작점을 전진하고
K만큼의 1이 없으면 끝점을 전진하는 방식으로 진행하였고
마지막에 시작점 또한 N으로 보내는 방식으로 나머지 경우의 수를 확인하였음
"""
N, K = map(int, input().split())
dolls = list(map(int, input().split()))

i, j = 0, K
cnt = sum(doll == 1 for doll in dolls[i:j])
min_serial_dolls = N + 1 if cnt < K else K
while j < N:
    if cnt >= K and i < j:
        cnt -= dolls[i] == 1
        i += 1
    else:
        cnt += dolls[j] == 1
        j += 1
    if cnt >= K:
        min_serial_dolls = min(min_serial_dolls, j - i)
while cnt >= K:
    cnt -= dolls[i] == 1
    i += 1
    if cnt >= K:
        min_serial_dolls = min(min_serial_dolls, j - i)
print(min_serial_dolls if min_serial_dolls <= N else -1)