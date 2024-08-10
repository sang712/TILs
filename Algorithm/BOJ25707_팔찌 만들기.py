"""
이렇게 편법이나 규칙을 발견해서 쉽게 풀 수 있으면 애드 혹 문제
구슬을 임의로 배치했을 때 
가장 값이 작은 구슬에서 가장 값이 큰 구슬의 거리는 무조건 둘의 차이고
가장 값이 큰 구슬에서 가장 값이 작은 구슬의 거리도 또한 같으므로
결과는 2*(max-min)이라고 할 수 있음
"""
N = int(input())
marble = list(map(int, input().split()))

print(2*(max(marble)-min(marble)))