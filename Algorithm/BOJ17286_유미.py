"""
가장 가까운 데부터 이동할 경우 좌우로 왔다 갔다 하는 경우가 생길 수 있어
어차피 경우의 수도 6개 밖에 안 되기 때문에 전부 확인해서 비교를 하는 방식을 사용했음
경우의 수는 itertools의 permutations 함수를 사용했고, 이를 이용해
각 순서대로 거리를 모두 더해 비교하였음
결과는 int를 씌워 소숫점은 버렸음
"""
import itertools
x0, y0 = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(3)]

ans = 1201
for perm in itertools.permutations([0, 1, 2]):
    temp_ans = 0
    last_x, last_y = x0, y0
    for idx in perm:
        x, y = people[idx][0], people[idx][1]
        temp_ans += (abs(last_x - x)**2 + abs(last_y - y)**2) ** 0.5
        last_x, last_y = x, y
    ans = min(temp_ans, ans)
print(int(ans))
