"""
조건의 분기를 나눌 때 같은 방향일 경우를 우선 나눴고 
그 후에 남북, 동서 방향으로 나누어 조건을 따졌음
같은 남<->북, 동<->서 이면 두 방향 모두 계산해서 낮은 값을 사용했고
다른 방향일 경우 왼쪽에서 맞닿는지, 오른쪽에서 맞닿는지 판단하기 위해 분기를 나눠주었음
"""
import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())
stores = [list(map(int, input().split())) for _ in range(n)]
dlocation, ddistance = map(int, input().split())

ans = 0
for location, distance in stores:
    if dlocation == location:
        ans += abs(ddistance - distance)
    elif dlocation <= 2:
        if location <= 2:
            ans += min(ddistance + distance, 2*w - (ddistance + distance)) + h
        else:
            distance = distance if dlocation == 1 else h - distance
            if location == 3:
                ans += ddistance + distance
            else:
                ans += w - ddistance + distance
    else:
        if location >= 3:
            ans += min(ddistance + distance, 2*h - (ddistance + distance)) + w
        else:
            distance = distance if dlocation == 3 else w - distance
            if location == 1:
                ans += ddistance + distance
            else:
                ans += h - ddistance + distance
print(ans)