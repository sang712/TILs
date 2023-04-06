"""
이틀 전에 풀었던 수열 문제와 같은 방식으로 풀되
리스트에 넣어 최댓값을 구하면 추가적인 연산이 필요하게 되므로
바로바로 최댓값인지 확인하여 최댓값의 개수를 카운트 하였음

Counter 객체를 사용한다면 더 나은 성능을 기대할 수도 있겠음
"""
N, X = map(int, input().split())
visitors = list(map(int, input().split()))

i, j = 0, X
total_visitors = sum(visitors[i:j])
max_visitors = total_visitors
period_max_visitors = 1
while j < N:
    total_visitors += - visitors[i] + visitors[j]
    if max_visitors < total_visitors:
        max_visitors = total_visitors
        period_max_visitors = 1
    elif max_visitors == total_visitors:
        period_max_visitors += 1
    i += 1
    j += 1
if max_visitors:
    print(max_visitors)
    print(period_max_visitors)
else:
    print('SAD')