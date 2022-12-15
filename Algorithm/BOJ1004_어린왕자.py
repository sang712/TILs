'''
시작점과 출발점이 원(행성계) 안에 존재하는지 그렇지 않은지만 판별하면 되어서
원점의 x거리 y거리를 각각 제곱해서 더한 것이 원의 반지름의 제곱보다 작으면 카운트 하도록 하였고
시작점과 출발점이 같은 원 안에 포함되는 경우도 있으므로 해당 경우를 따로 체크하여 오답을 방지하였음
'''
import sys
input = sys.stdin.readline

T = int(input())

def is_in_circle(x, y, cx, cy, r):
    return abs(x-cx)**2 + abs(y-cy)**2 < r**2


for tc in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    
    cnt = 0
    for i in range(n):
        cx, cy, r = map(int, input().split())
        if is_in_circle(x1, y1, cx, cy, r):
            if is_in_circle(x2, y2, cx, cy, r):
                continue
            else:
                cnt += 1
        elif is_in_circle(x2, y2, cx, cy, r):
            cnt += 1
    print(cnt)