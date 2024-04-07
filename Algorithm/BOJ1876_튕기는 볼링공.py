"""
x가 T를 지나는 구간을 찾아서 y를 스텝 1씩 변화시키는 방식으로
원의 부등식을 이용해 풀이했었는데 틀린 답을 내서
답을 찾아보았음
해당 답은 굳이 스텝으로 1씩 증가시키는 것이 아니라 y의 위치가 0일 때만을 판단하며
y의 위치가 0일 때마다 x의 위치는 같은 단위별로 증가하므로 x의 좌표를 구하기 쉬움
다만 이 때 주의할 점은 볼링공과 핀의 중앙의 값을 단순 비교하는 것이 아니라
볼링공의 전진 방향을 고려하여 T에 16/sin(degree)의 차이로 비교하는 것임
이 것은 두 원의 접점에서 각 원(볼링공과 핀)의 거리를 구해 합한 것(10/sin(degree) + 6/sin(degree))과 같음
"""
import sys
import math
input = sys.stdin.readline

N = int(input())
for case in range(N):
    T, degree = input().split()
    T = int(float(T)*100)
    degree = math.radians(int(degree))
    dist = 42.5 / math.tan(degree)
    x = 0
    while x < T + 16/math.sin(degree):
        if T - 16/math.sin(degree) <= x <= T + 16/math.sin(degree):
            print('yes')
            break
        x += 2*dist
    else:
        print('no')