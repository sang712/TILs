"""
주어진 문제가 빙빙 돌려서 설명되어있는데 
결과적으로 임의의 세 점을 이용해 삼각형을 만들었을 때 최대 넓이를 구하라는 문제임
삼각형을 구하는 공식을 적용해 풀이하였음
"""
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

def S(x1, y1, x2, y2, x3, y3):
    return abs((x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x2*y1 + x3*y2))/2

ans = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            ans = max(ans, S(*points[i], *points[j], *points[k]))
print(f'{ans:.1f}')