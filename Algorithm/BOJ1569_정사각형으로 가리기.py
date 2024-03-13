"""
주어진 점들로 얻은 가로 길이의 값과, 세로 길이의 값이 다를 경우를 고려하지 않아서 틀린답을 냈었고
정사각형이기 때문에 가로 길이의 값과 세로 길이의 값이 같도록 만들어서 풀이하였음
"""
N = int(input())

points = [tuple(map(int, input().split())) for _ in range(N)]
points.sort()
min_x, max_x = points[0][0], points[-1][0]
points.sort(key=lambda point: point[1])
min_y, max_y = points[0][1], points[-1][1]

def are_points_on(min_x, max_x, min_y, max_y):
    for i in range(N):
        x, y = points[i]
        if (x == min_x or x == max_x) and min_y <= y <= max_y:
            continue
        elif (y == min_y or y == max_y) and min_x <= x <= max_x:
            continue
        else:
            return False
    return True

gap = max(max_x - min_x, max_y - min_y)
if max_x - min_x == max_y - min_y:
    if are_points_on(min_x, max_x, min_y, max_y): print(gap)
    else: print(-1)
elif gap == max_y - min_y:
    if are_points_on(max_x-gap, max_x, min_y, max_y) or are_points_on(min_x, min_x+gap, min_y, max_y): print(gap)
    else: print(-1)
elif gap == max_x - min_x: 
    if are_points_on(min_x, max_x, max_y-gap, max_y) or are_points_on(min_x, max_x, min_y, min_y+gap): print(gap)
    else: print(-1)
else: 
    print(-1)