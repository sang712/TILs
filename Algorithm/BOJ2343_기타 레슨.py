"""
딱 보고 이분 탐색 문제라고 판단하여 정형적으로 구현했고
한 번 틀렸는데 주어진 강의의 길이가 블루레이의 길이보다 큰 경우 
무조건 false를 반환해야 하는데 이 부분을 간과하였음

추가로 left를 0으로 시작할 때 while문의 부호에 같다를 추가하거나 else문의 left에 + 1을 해주면
무한 루프가 도는 문제가 있음
근데 답은 절대 0이 나올 수 없으므로 1로 시작하는 것이 맞긴 함
"""
N, M = map(int, input().split())
lesson = list(map(int, input().split()))

def burn(max_len):
    cnt = 1
    cd = 0
    for min in lesson:
        cd += min
        if cd > max_len:
            cnt += 1
            cd = min
        if cnt > M or cd > max_len:
            return False
    return True

ans = 1_000_000_000
left, right = 1, 1_000_000_000
while left <= right:
    mid = (left + right) // 2
    if burn(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
print(ans)