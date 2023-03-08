"""
13개의 경우로 조합을 만들면 1716가지가 최대이므로
2500 * 1716 으로 얼추 어림잡아 100만가지의 경우가 나옴
따라서 시간 복잡도 상관없이 그냥 구현하면 됨
도시 정보를 받아올 때, 집의 위치와 치킨 집의 위치를 따로 받아왔고
집의 위치와 치킨집의 위치의 차이의 절대값을 이용해 치킨 거리를 구하도록 하였음
이 때 폐점할 치킨집은 itertools의 조합 함수를 import하여 적용하였음
"""
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

city = [input().split() for _ in range(N)]
chicken_franchise = set()
houses = []
for i in range(N):
    for j in range(N):
        if city[i][j] == '2':
            chicken_franchise.add((i, j))
        elif city[i][j] == '1':
            houses.append((i,j))

def count_chicken_dist():
    city_chicken_dist = 0
    for i, j in houses:
        chicken_dist = min(list(map(lambda pos: abs(pos[0]-i) + abs(pos[1]-j), chicken_franchise)))
        city_chicken_dist += chicken_dist
      
    return city_chicken_dist

min_city_chicken_dist = 2501
num_shut_down = len(chicken_franchise) - M
for shutting_down in combinations(chicken_franchise, num_shut_down):
    for r, c in shutting_down:
        chicken_franchise.discard((r, c))
    min_city_chicken_dist = min(min_city_chicken_dist, count_chicken_dist())
    for r, c in shutting_down:
        chicken_franchise.add((r, c))

print(min_city_chicken_dist)