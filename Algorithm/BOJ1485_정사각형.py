"""
한 점에서 각 점까지의 거리의 제곱을 구하고
가장 작은 것 2개의 합이 가장 긴 것과 같은 경우에 조건을 만족한다고 했었는데
각 변의 제곱이 같지 않을 수도 있어서 해당 부분을 추가하여 통과하였음
추가로 시간이 다른 사람의 4배여서 로직을 바꿔보다가 
input의 방식을 바꾸었더니 로직이 어떻든 48ms로 줄어들어서 다른 사람보다 빠르게 풀이할 수 있었음
"""
import sys
input = sys.stdin.readline

for case in range(int(input())):
    points = [tuple(map(int, input().split())) for _ in range(4)]
    for _ in range(2):
        dists = []
        for i in range(1, 4):
            dists.append((points[0][0] - points[i][0])**2 + (points[0][1] - points[i][1])**2)
        dists.sort()
        if not sum(dists[:2]) == dists[2] or not dists[0] == dists[1]:
            print(0)
            break
        points = points[1:] + [points[0]]
    else:
        print(1)