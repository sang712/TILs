"""
오름차순 정렬한 것과 기존의 것을 비교하고
내림차순 정렬한 것과 기존의 것을 비교한 뒤 같을 경우에 해당 정렬을 출력하고
아니면 둘다 아니라고 출력하도록 하였음
"""
N = int(input())

athletes = [input() for _ in range(N)]
if athletes == sorted(athletes):
    print('INCREASING')
elif athletes == sorted(athletes, reverse=True):
    print('DECREASING')
else:
    print('NEITHER')