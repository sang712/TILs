"""
어떻게 풀지 몰라서 간단하게 생각해낼 수 있는 이분탐색으로 풀었음

더 빠른 풀이를 찾아보니
한번만 완전탐색해서 풀이하는 방법이 있었음
우선 다운로드 하는 시간(ans)과 다운로드한 음악 재생 시간(play)을 각각 변수로 지정하고 처음 입력값을 초기값으로 넣어 놓음
그 후에 탐색을 하면서 
play보다 다음 조각을 다운로드할 시간이 더 길다면
ans에 다음 조각을 다운로드할 시간과 play의 차를 더해주고 play를 이번에 다운로드한 조각의 재생 시간으로 초기화 함

다음 조각을 다운로드할 시간이 같거나 작다면
play에 다음 조각을 다운로드할 시간을 빼주고 다음 조각의 재생 시간을 더해줌
"""
import sys
input = sys.stdin.readline

N = int(input())

song_pieces = [tuple(map(int, input().split())) for _ in range(N)]

def is_possible(download_time):
    time = download_time
    for d, v in song_pieces:
        if time >= v:
            time += d - v
        else:
            return False
    return True

ans = 100_000_000
left, right = 0, 100_000_000
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1
print(ans)