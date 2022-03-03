N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for _ in range(N):
    if _ > 0:
        arr[_][0] += arr[_-1][0]
for _ in range(M):
    if _ > 0:
        arr[0][_] += arr[0][_-1] # 이 라인을 8번 라인을 복사해서 만들다보니 우항의 인덱스를 바꾸지 않은 실수를 함

for r in range(1, N):
    for c in range(1, M):
        # if문으로 나누는 거 보다 max 함수를 사용해서 적용하는 것이 더 좋음
        arr[r][c] += max(arr[r-1][c], arr[r][c-1])
print(arr[N-1][M-1])