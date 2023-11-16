"""
~~다 더해서 평균 낸 뒤에 계산하면 될 것 같음~~
~~근데 그렇게 하면 미지수가 2개 라서 안됨 가 아니라 평균 하는 것이 맞았음~~

a와 b의 범위가 100 이하의 양의 정수로 범위가 정해져 있으므로 그냥 브루트 포스로 확인하면 됨
rss를 각각 계산하여 풀이하면 됨

1. a와 b의 range를 101까지 잡지 않은 점
2. 각각의 rss를 계산하는 것이 아닌 그냥 한번에 더해서 퉁치려고 했던 점
3. 최대가 될 수 있는 rss의 총합은 1000 * 100의 제곱 * 점의 개수 이므로 10 ** 12 가 넘음
3-1. 근데 10 ** 9만 해도 통과할 수 있었음
"""
import sys
input = sys.stdin.readline

N = int(input())

points = [list(map(int, input().split())) for _ in range(N)]

min_rss = 10 ** 9
ans = (100, 100)
for a in range(1, 101):
    for b in range(1, 101):
        rss = 0
        for x, y in points:
            rss += (y - a*x - b) ** 2
        if rss < min_rss:
            ans = (a, b)
            min_rss = rss
print(*ans)