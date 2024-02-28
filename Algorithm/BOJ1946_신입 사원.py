"""
처음 등수로 정렬을 하여 다음 등수를 순서대로 확인하면서
현재까지 나온 최고 등수보다 낮으면 제외하는 방식을 이용하였음

처음 등수 정렬, 다음 등수 정렬 각각 진행하는 방식을 이용했다가
1번만 해도 유효하다는 것을 깨달아서 한번으로 수정하였고
두 번 정렬을 위해 도입했던 pass/fail 리스트를 제거하고 그냥 카운팅 변수를 추가하였음
"""
import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    N = int(input())
    candidates = [tuple(map(int, input().split())) for _ in range(N)]
    passed = 0

    by_docu = sorted(candidates, key=lambda x: x[0])
    lowest_rank = N
    for docu, inter in by_docu:
        if inter <= lowest_rank:
            passed += 1
        lowest_rank = min(lowest_rank, inter)
    print(passed)