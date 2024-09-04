"""
우선 곱하기를 하고 나머지를 구하나
각각의 나머지를 구해고 곱하는 과정으로 나머지를 구하나 결과는 같음
여기에 N이 M보다 큰 경우 나누어 떨어지므로 나머지는 0이 됨
위의 방법을 적용하여 문제를 풀이하였음
"""
N, M = map(int, input().split())
if N >= M:
    print(0)
else:
    ans = 1
    for i in range(1, N+1):
        ans *= i
        ans %= M
    print(ans)