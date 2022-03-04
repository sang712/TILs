N, K = map(int, input().split())
course = list(map(int, input().split()))

running = 0
ans = -1
# 정방향
for idx in range(len(course)):
    track = course[idx]
    if running <= K < running+track:
        ans = idx + 1  # 인덱스 값이 1 작으므로 1을 더해줌
        break
    else:
        running += track
# 역방향
if ans < 0:
    for idx in range(len(course)-1, -1, -1):
        track = course[idx]
        if running < K <= running+track:
            ans = idx + 1  # 인덱스 값이 1 작으므로 1을 더해줌
            break
        else:
            running += track
print(ans)